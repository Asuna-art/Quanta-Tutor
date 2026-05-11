"""agent.py - 金融数学智能学伴的 Agent 主程序

实现:
  - 实验一:Agent Loop + 工具调用
  - 实验二:RAG 知识库注入(SYSTEM_PROMPT 注入 + RAG 工具调用)
  - 大作业新增工具:计算器、利率/年金/贷款/NPV/久期等专用计算器、
    出题、判分、错题记录、学习画像、学习计划生成。
"""
from __future__ import annotations

import json
import math
import os
import re
import time
import uuid
from pathlib import Path
from typing import Any, Callable

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

from rag_library import RAGLibrary, load_or_build_rag_library

# ------------------------------------------------------------------
# 配置
# ------------------------------------------------------------------
load_dotenv(override=True)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LIBRARY_DIR = PROJECT_ROOT / "library"
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

CHAT_MODEL = os.getenv("CHAT_MODEL", "qwen-plus")
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-v4")
RAG_TOP_K = int(os.getenv("RAG_TOP_K", "4"))
RAG_MIN_SCORE = float(os.getenv("RAG_MIN_SCORE", "0.2"))

SYSTEM_PROMPT = """你是「金融数学智能学伴」,一名专业、耐心、循循善诱的助教,服务于本科/精算《金融数学》(Financial Mathematics)课程。

你的职责:
1. 知识问答:对学生提出的概念/原理/公式问题给出"定义—原理—示例—易错点"的结构化回答。
2. 学习诊断:根据学生的提问历史、错题、测验结果,识别薄弱知识点,给出具体的学习画像。
3. 个性化练习:围绕薄弱点出题(选择题/填空题/计算题),并对学生答题进行判分、错因分析、改进建议。
4. 学习规划:结合学生目标(考研/期末/精算考试)和时间预算,给出阶段性复习计划。

行为准则:
- 涉及到具体公式计算时,优先调用 `calc_*` 工具来获得准确的数值结果,不要靠心算。
- 涉及到课程定义、章节内容、概念解释时,优先调用 `search_knowledge` 检索知识库,引用原文佐证。
- 涉及到学情、错题、画像时,调用 `get_learning_profile` 等工具读取真实数据,不要编造。
- 出题时使用 `generate_exercise`;学生提交答案后用 `grade_exercise` 判分。
- 回答风格:有条理、用 Markdown,公式用 LaTeX($...$ 行内,$$...$$ 块级)。"""


# ------------------------------------------------------------------
# 模型客户端
# ------------------------------------------------------------------
def make_client() -> OpenAI:
    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("API_KEY")
    if not base_url or not api_key:
        raise EnvironmentError(
            "请在 .env 中设置 BASE_URL 和 API_KEY (例如 qwen 的 https://dashscope.aliyuncs.com/compatible-mode/v1)。"
        )
    return OpenAI(base_url=base_url, api_key=api_key)


# ==================================================================
# 工具实现层
# ==================================================================

# ---------- 1. 通用计算器 ----------
_SAFE_MATH_NAMES = {
    k: getattr(math, k)
    for k in [
        "sqrt", "log", "log2", "log10", "exp", "pow",
        "sin", "cos", "tan", "asin", "acos", "atan",
        "pi", "e", "floor", "ceil", "fabs",
    ]
}
_SAFE_MATH_NAMES["abs"] = abs


def calc_eval(expression: str) -> str:
    """安全地计算一个数学表达式。支持 +-*/、**、math.sqrt/log/exp 等。"""
    expr = expression.strip()
    if not re.fullmatch(r"[0-9eE\.\+\-\*\/\(\)\,\s\^a-zA-Z_]*", expr):
        return f"表达式包含不允许的字符: {expression!r}"
    expr = expr.replace("^", "**")
    try:
        value = eval(expr, {"__builtins__": {}}, _SAFE_MATH_NAMES)
        if isinstance(value, complex):
            return str(value)
        return f"{value:.10g}"
    except Exception as e:  # noqa: BLE001
        return f"计算失败: {e}"


# ---------- 2. 金融数学专用计算器 ----------
def calc_compound(principal: float, rate: float, years: float, compounding: str = "annual") -> str:
    """复利累积值。compounding ∈ {annual, semiannual, quarterly, monthly, continuous}"""
    if rate < -1:
        return "利率不能小于 -100%"
    if compounding == "continuous":
        fv = principal * math.exp(rate * years)
    else:
        m_map = {"annual": 1, "semiannual": 2, "quarterly": 4, "monthly": 12, "weekly": 52, "daily": 365}
        m = m_map.get(compounding, 1)
        fv = principal * (1 + rate / m) ** (m * years)
    return json.dumps(
        {"principal": principal, "rate": rate, "years": years,
         "compounding": compounding, "future_value": round(fv, 6)},
        ensure_ascii=False,
    )


def calc_present_value(future_value: float, rate: float, years: float, compounding: str = "annual") -> str:
    """现值 PV = FV / (1+i)^n。"""
    if compounding == "continuous":
        pv = future_value * math.exp(-rate * years)
    else:
        m_map = {"annual": 1, "semiannual": 2, "quarterly": 4, "monthly": 12}
        m = m_map.get(compounding, 1)
        pv = future_value / (1 + rate / m) ** (m * years)
    return json.dumps(
        {"future_value": future_value, "rate": rate, "years": years,
         "compounding": compounding, "present_value": round(pv, 6)},
        ensure_ascii=False,
    )


def calc_annuity(payment: float, rate: float, periods: int,
                 kind: str = "ordinary") -> str:
    """
    年金现值与累积值。
      kind = "ordinary"(期末年金 a_n)或 "due"(期初年金 ä_n)。
    """
    i = rate
    n = periods
    if abs(i) < 1e-12:
        a_n = float(n)
        s_n = float(n)
    else:
        v = 1.0 / (1 + i)
        a_n = (1 - v ** n) / i
        s_n = ((1 + i) ** n - 1) / i

    if kind == "due":
        a_due = a_n * (1 + i)
        s_due = s_n * (1 + i)
        pv = payment * a_due
        fv = payment * s_due
        formula = "PV = P · ä_n = P · (1-v^n)/d"
    else:
        pv = payment * a_n
        fv = payment * s_n
        formula = "PV = P · a_n = P · (1-v^n)/i"

    return json.dumps(
        {"payment": payment, "rate": rate, "periods": periods, "kind": kind,
         "a_n": round(a_n, 6), "s_n": round(s_n, 6),
         "present_value": round(pv, 6), "future_value": round(fv, 6),
         "formula": formula},
        ensure_ascii=False,
    )


def calc_loan_payment(principal: float, rate: float, periods: int) -> str:
    """等额还款贷款的每期还款额: P = L / a_n。返回还款表前几期。"""
    i = rate
    n = periods
    if abs(i) < 1e-12:
        pmt = principal / n
    else:
        a_n = (1 - (1 + i) ** -n) / i
        pmt = principal / a_n

    schedule = []
    balance = principal
    for k in range(1, min(n, 12) + 1):
        interest = balance * i
        principal_pay = pmt - interest
        balance = balance - principal_pay
        schedule.append({
            "period": k,
            "payment": round(pmt, 4),
            "interest": round(interest, 4),
            "principal": round(principal_pay, 4),
            "balance": round(max(balance, 0.0), 4),
        })
    return json.dumps(
        {"principal": principal, "rate": rate, "periods": periods,
         "level_payment": round(pmt, 6),
         "schedule_first_periods": schedule,
         "note": f"展示前 {len(schedule)} 期; 共 {n} 期"},
        ensure_ascii=False,
    )


def calc_npv(rate: float, cashflows: list[float]) -> str:
    """
    净现值。cashflows[k] 表示第 k 期(k=0,1,2,...)的现金流。
    NPV = Σ C_k / (1+i)^k
    """
    npv = sum(c / (1 + rate) ** k for k, c in enumerate(cashflows))
    return json.dumps(
        {"rate": rate, "cashflows": cashflows, "npv": round(npv, 6)},
        ensure_ascii=False,
    )


def calc_irr(cashflows: list[float], guess: float = 0.1) -> str:
    """内部收益率,Newton 迭代;失败则二分回退。"""
    def npv(r: float) -> float:
        return sum(c / (1 + r) ** k for k, c in enumerate(cashflows))

    def dnpv(r: float) -> float:
        return sum(-k * c / (1 + r) ** (k + 1) for k, c in enumerate(cashflows))

    r = guess
    for _ in range(80):
        f = npv(r)
        fp = dnpv(r)
        if abs(fp) < 1e-12:
            break
        r_new = r - f / fp
        if r_new <= -0.999:
            r_new = (r - 0.999) / 2
        if abs(r_new - r) < 1e-10:
            r = r_new
            break
        r = r_new

    if not math.isfinite(r) or abs(npv(r)) > 1e-4:
        # 二分回退
        lo, hi = -0.99, 10.0
        f_lo, f_hi = npv(lo), npv(hi)
        if f_lo * f_hi > 0:
            return json.dumps({"error": "IRR 在 [-99%, 1000%] 区间内未找到根",
                               "cashflows": cashflows}, ensure_ascii=False)
        for _ in range(200):
            mid = (lo + hi) / 2
            f_mid = npv(mid)
            if abs(f_mid) < 1e-10:
                r = mid
                break
            if f_lo * f_mid < 0:
                hi, f_hi = mid, f_mid
            else:
                lo, f_lo = mid, f_mid
        r = (lo + hi) / 2

    return json.dumps(
        {"cashflows": cashflows, "irr": round(r, 8),
         "npv_at_irr": round(npv(r), 6)},
        ensure_ascii=False,
    )


def calc_bond_price(face_value: float, coupon_rate: float,
                    yield_rate: float, periods: int,
                    frequency: int = 1) -> str:
    """债券定价: P = Σ Coupon · v^t + F · v^n。frequency 为每年付息次数。"""
    m = frequency
    coupon = face_value * coupon_rate / m
    n = periods * m
    y = yield_rate / m
    v = 1.0 / (1 + y)
    if abs(y) < 1e-12:
        a_n = float(n)
    else:
        a_n = (1 - v ** n) / y
    price = coupon * a_n + face_value * v ** n
    return json.dumps(
        {"face_value": face_value, "coupon_rate": coupon_rate,
         "yield_rate": yield_rate, "periods_years": periods,
         "frequency_per_year": frequency,
         "price": round(price, 6),
         "coupon_per_period": round(coupon, 6)},
        ensure_ascii=False,
    )


def calc_duration(cashflows: list[float], times: list[float],
                  yield_rate: float) -> str:
    """Macaulay 久期 D 和修正久期 D_M = D/(1+y)。"""
    if len(cashflows) != len(times):
        return json.dumps({"error": "cashflows 与 times 长度不一致"})
    pv = [c / (1 + yield_rate) ** t for c, t in zip(cashflows, times)]
    price = sum(pv)
    if price == 0:
        return json.dumps({"error": "价格为 0,无法计算久期"})
    macaulay = sum(t * p for t, p in zip(times, pv)) / price
    modified = macaulay / (1 + yield_rate)
    convexity = sum(t * (t + 1) * c / (1 + yield_rate) ** (t + 2)
                    for c, t in zip(cashflows, times)) / price
    return json.dumps(
        {"yield_rate": yield_rate, "price": round(price, 6),
         "macaulay_duration": round(macaulay, 6),
         "modified_duration": round(modified, 6),
         "convexity": round(convexity, 6)},
        ensure_ascii=False,
    )


def calc_force_of_interest(rate: float) -> str:
    """利率力 δ = ln(1+i),以及对应贴现率 d 和贴现因子 v。"""
    if rate <= -1:
        return json.dumps({"error": "i 必须 > -1"})
    delta = math.log(1 + rate)
    d = rate / (1 + rate)
    v = 1.0 / (1 + rate)
    return json.dumps(
        {"effective_rate_i": rate,
         "force_of_interest_delta": round(delta, 8),
         "discount_rate_d": round(d, 8),
         "discount_factor_v": round(v, 8)},
        ensure_ascii=False,
    )


def calc_nominal_to_effective(nominal: float, p: int) -> str:
    """名义利率 i^(p) -> 实际年利率: (1 + i^(p)/p)^p - 1。"""
    if p <= 0:
        return json.dumps({"error": "p 必须 > 0"})
    eff = (1 + nominal / p) ** p - 1
    return json.dumps(
        {"nominal_rate_i_p": nominal, "p": p,
         "effective_annual_rate_i": round(eff, 10)},
        ensure_ascii=False,
    )


# ---------- 3. RAG 知识库检索工具 ----------
RAG_LIBRARY: RAGLibrary | None = None  # 在 __main__ 中注入


def search_knowledge(query: str, top_k: int = 4) -> str:
    """从课程讲义检索与 query 最相关的若干文本片段。"""
    if RAG_LIBRARY is None:
        return "[error] 知识库未初始化"
    results = RAG_LIBRARY.search(query, top_k=int(top_k))
    if not results:
        return "[no result]"
    out = []
    for chunk, score in results:
        out.append({
            "source": chunk.source,
            "chunk_index": chunk.index,
            "score": round(score, 4),
            "content": chunk.content[:1200],
        })
    return json.dumps(out, ensure_ascii=False)


# ---------- 4. 学情/学习画像/错题记录 ----------
TOPIC_KEYWORDS: dict[str, list[str]] = {
    "ch1_modeling":     ["model", "模型", "cashflow", "现金流", "建模", "actuarial"],
    "ch2_interest":     ["利率", "interest", "compound", "复利", "force of interest", "利率力", "discount", "贴现"],
    "ch3_annuities":    ["annuity", "年金", "a_n", "s_n", "equation of value", "价值方程", "deferred"],
    "ch4_loan":         ["loan", "贷款", "schedule", "还款", "amortization", "本息"],
    "ch5_appraisal":    ["NPV", "净现值", "IRR", "内部收益率", "payback", "回收期", "inflation", "通胀"],
    "ch6_bonds":        ["bond", "债券", "coupon", "息票", "yield", "redemption", "capital gain", "index-linked"],
    "ch7_term":         ["term structure", "期限结构", "spot", "现货", "forward", "远期", "duration", "久期",
                         "convexity", "凸度", "immunisation", "免疫"],
    "ch8_expectations": ["rational expectations", "理性预期", "efficient market", "有效市场"],
}

TOPIC_NAMES = {
    "ch1_modeling":     "第1章 数据与金融建模",
    "ch2_interest":     "第2章 利率介绍(单利/复利/利率力)",
    "ch3_annuities":    "第3章 年金与价值方程",
    "ch4_loan":         "第4章 贷款偿还表",
    "ch5_appraisal":    "第5章 投资项目评估(NPV/IRR/通胀)",
    "ch6_bonds":        "第6章 固定利率证券",
    "ch7_term":         "第7章 利率期限结构(久期/凸度/免疫)",
    "ch8_expectations": "第8章 理性预期理论",
}


def _classify_topic(text: str) -> list[str]:
    text_lower = text.lower()
    hits = []
    for topic, kws in TOPIC_KEYWORDS.items():
        for kw in kws:
            if kw.lower() in text_lower:
                hits.append(topic)
                break
    return hits


PROFILE_PATH = DATA_DIR / "learning_profile.json"


def _load_profile() -> dict:
    if PROFILE_PATH.exists():
        return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
    return {
        "questions_asked": [],   # [{ts, query, topics}]
        "wrong_answers": [],     # [{ts, exercise_id, topic, your_answer, correct_answer, explanation}]
        "exercise_history": [],  # [{ts, exercise_id, topic, correct}]
        "topic_stats": {},       # topic -> {asked, attempted, correct, wrong}
    }


def _save_profile(profile: dict) -> None:
    PROFILE_PATH.write_text(
        json.dumps(profile, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def log_question(query: str) -> str:
    """记录一次学生提问及其涉及的主题(供后台调用,不暴露给学生)。"""
    profile = _load_profile()
    topics = _classify_topic(query)
    profile["questions_asked"].append({
        "ts": int(time.time()),
        "query": query,
        "topics": topics,
    })
    for t in topics:
        profile["topic_stats"].setdefault(t, {"asked": 0, "attempted": 0, "correct": 0, "wrong": 0})
        profile["topic_stats"][t]["asked"] += 1
    _save_profile(profile)
    return json.dumps({"ok": True, "topics": topics}, ensure_ascii=False)


def get_learning_profile() -> str:
    """返回当前学生的学习画像(提问主题分布、错题、各章节正确率等)。"""
    profile = _load_profile()
    summary = {
        "total_questions": len(profile["questions_asked"]),
        "total_exercises": len(profile["exercise_history"]),
        "wrong_count": len(profile["wrong_answers"]),
        "by_topic": {},
        "weakest_topics": [],
        "recent_questions": [q["query"] for q in profile["questions_asked"][-5:]],
        "recent_wrong": profile["wrong_answers"][-5:],
    }
    for topic, stats in profile["topic_stats"].items():
        attempted = stats["attempted"]
        accuracy = (stats["correct"] / attempted) if attempted > 0 else None
        summary["by_topic"][topic] = {
            "name": TOPIC_NAMES.get(topic, topic),
            "asked": stats["asked"],
            "attempted": attempted,
            "correct": stats["correct"],
            "wrong": stats["wrong"],
            "accuracy": round(accuracy, 3) if accuracy is not None else None,
        }
    # 找薄弱:正确率<60% 或 错题占比高的主题
    weak = []
    for topic, info in summary["by_topic"].items():
        if info["attempted"] >= 2 and info["accuracy"] is not None and info["accuracy"] < 0.6:
            weak.append((info["accuracy"], topic, info))
    weak.sort()
    summary["weakest_topics"] = [
        {"topic": t, "name": TOPIC_NAMES.get(t, t), **info}
        for _, t, info in weak[:3]
    ]
    return json.dumps(summary, ensure_ascii=False)


# ---------- 5. 出题与判分 ----------
EXERCISE_BANK_PATH = DATA_DIR / "exercise_bank.json"
ACTIVE_EXERCISE_PATH = DATA_DIR / "active_exercise.json"


def _exercise_seed_bank() -> list[dict]:
    """初始化时使用的内置题库(让系统冷启动也可用)。"""
    return [
        # ----- 第2章:利率/复利 -----
        {
            "id": "Q2-1", "topic": "ch2_interest", "type": "single_choice",
            "stem": "某账户年实际利率 i=8%。存入 1000 元,2 年后的累积值是多少?",
            "options": ["A) 1160", "B) 1166.40", "C) 1180", "D) 1200"],
            "answer": "B",
            "explanation": "复利累积值 = 1000·(1+0.08)^2 = 1000·1.1664 = 1166.40。"
        },
        {
            "id": "Q2-2", "topic": "ch2_interest", "type": "fill_blank",
            "stem": "若年实际利率 i=10%,其对应的利率力 δ = ln(1+i) = ____ (保留 4 位小数)。",
            "answer": "0.0953",
            "explanation": "δ = ln(1.10) ≈ 0.09531,保留四位为 0.0953。"
        },
        {
            "id": "Q2-3", "topic": "ch2_interest", "type": "single_choice",
            "stem": "名义利率 i^(4)=12%(按季度复利),其等价的实际年利率是多少?",
            "options": ["A) 12.00%", "B) 12.36%", "C) 12.55%", "D) 12.68%"],
            "answer": "C",
            "explanation": "(1+0.12/4)^4-1 = 1.03^4-1 ≈ 0.12551 ≈ 12.55%。"
        },
        # ----- 第3章:年金 -----
        {
            "id": "Q3-1", "topic": "ch3_annuities", "type": "single_choice",
            "stem": "在 i=5% 下,期末支付 1 元、期数 10 年的年金现值 a_10 ≈ ?",
            "options": ["A) 7.7217", "B) 8.1109", "C) 6.4632", "D) 9.6361"],
            "answer": "A",
            "explanation": "a_n = (1-v^n)/i = (1-1.05^-10)/0.05 ≈ 7.7217。"
        },
        {
            "id": "Q3-2", "topic": "ch3_annuities", "type": "calculation",
            "stem": "年实际利率 i=6%,期末年金每年支付 2000 元,共 5 年。求其现值。",
            "answer": "8424.73",
            "explanation": "PV = 2000·a_5|6% = 2000·(1-1.06^-5)/0.06 ≈ 2000·4.21236 ≈ 8424.73。"
        },
        # ----- 第4章:贷款 -----
        {
            "id": "Q4-1", "topic": "ch4_loan", "type": "calculation",
            "stem": "贷款 100000 元,年利率 i=5%,等额还款 20 年。每年还款额是多少?",
            "answer": "8024.26",
            "explanation": "P = 100000/a_20|5% = 100000 / 12.46221 ≈ 8024.26。"
        },
        # ----- 第5章:NPV/IRR -----
        {
            "id": "Q5-1", "topic": "ch5_appraisal", "type": "single_choice",
            "stem": "项目现金流 (年 0,1,2): -1000, 600, 600,贴现率 i=10%。NPV 约为?",
            "options": ["A) -83.47", "B) 41.32", "C) 41.32", "D) 200.00"],
            "answer": "B",
            "explanation": "NPV = -1000 + 600/1.1 + 600/1.21 ≈ -1000 + 545.45 + 495.87 ≈ 41.32。"
        },
        {
            "id": "Q5-2", "topic": "ch5_appraisal", "type": "fill_blank",
            "stem": "若 NPV(i)=0 时 i=8%,则该项目的内部收益率 IRR = ____。",
            "answer": "8%",
            "explanation": "IRR 的定义就是使 NPV=0 的折现率。"
        },
        # ----- 第6章:债券 -----
        {
            "id": "Q6-1", "topic": "ch6_bonds", "type": "single_choice",
            "stem": "票面利率高于到期收益率(YTM)时,债券价格相对于面值会:",
            "options": ["A) 平价", "B) 折价(<面值)", "C) 溢价(>面值)", "D) 无法判断"],
            "answer": "C",
            "explanation": "票息率 g > YTM y 时,买家愿意支付高于面值的价格,即溢价。"
        },
        # ----- 第7章:期限结构/久期 -----
        {
            "id": "Q7-1", "topic": "ch7_term", "type": "single_choice",
            "stem": "下列关于 Macaulay 久期 D 与修正久期 D_M 的关系,正确的是:",
            "options": ["A) D_M = D·(1+y)", "B) D_M = D/(1+y)", "C) D_M = D - 1", "D) D_M = D"],
            "answer": "B",
            "explanation": "修正久期 D_M = D/(1+y),用于近似 ΔP/P ≈ -D_M·Δy。"
        },
        {
            "id": "Q7-2", "topic": "ch7_term", "type": "fill_blank",
            "stem": "Redington 免疫的三个条件中,要求资产凸度 ____ 负债凸度。(填'大于等于'或'小于')",
            "answer": "大于等于",
            "explanation": "Redington 三条件:PV 相等、Duration 相等,且资产凸度 >= 负债凸度。"
        },
        # ----- 第8章:理性预期 -----
        {
            "id": "Q8-1", "topic": "ch8_expectations", "type": "single_choice",
            "stem": "在理性预期假设下,预期误差应满足:",
            "options": ["A) 期望非零", "B) 与历史信息相关",
                        "C) 期望为零且与可得信息无关", "D) 服从均匀分布"],
            "answer": "C",
            "explanation": "理性预期要求预期误差具有零均值且不能由可得信息预测,否则就不是无偏预期。"
        },
    ]


def _load_bank() -> list[dict]:
    if EXERCISE_BANK_PATH.exists():
        return json.loads(EXERCISE_BANK_PATH.read_text(encoding="utf-8"))
    bank = _exercise_seed_bank()
    EXERCISE_BANK_PATH.write_text(json.dumps(bank, ensure_ascii=False, indent=2), encoding="utf-8")
    return bank


def generate_exercise(topic: str | None = None,
                      qtype: str | None = None,
                      difficulty: str | None = None) -> str:
    """
    从题库中挑一道题。topic 可为 None(自动选薄弱章节)或具体章节 key。
    qtype ∈ {single_choice, fill_blank, calculation}, 不指定则随机。
    """
    bank = _load_bank()
    profile = _load_profile()

    # 自动选薄弱章节
    if not topic:
        weak_topics = []
        for t, stats in profile["topic_stats"].items():
            if stats["attempted"] >= 1 and stats["wrong"] > 0:
                acc = stats["correct"] / max(stats["attempted"], 1)
                weak_topics.append((acc, t))
        if weak_topics:
            weak_topics.sort()
            topic = weak_topics[0][1]
        else:
            # 还没数据,默认 ch3
            topic = "ch3_annuities"

    candidates = [q for q in bank if q["topic"] == topic]
    if qtype:
        candidates = [q for q in candidates if q["type"] == qtype] or candidates

    # 排除最近已做过的
    done_ids = {h["exercise_id"] for h in profile["exercise_history"][-15:]}
    fresh = [q for q in candidates if q["id"] not in done_ids] or candidates
    if not fresh:
        return json.dumps({"error": f"题库中没有 {topic} 的题目"}, ensure_ascii=False)

    # 简单随机
    rnd_index = int(time.time() * 1000) % len(fresh)
    q = dict(fresh[rnd_index])

    # 写入 active(供 grade_exercise 读取答案)
    ACTIVE_EXERCISE_PATH.write_text(json.dumps(q, ensure_ascii=False), encoding="utf-8")

    # 不直接告诉模型答案,只回传题面+id,模型把题目展示给学生
    public = {k: v for k, v in q.items() if k not in {"answer", "explanation"}}
    public["topic_name"] = TOPIC_NAMES.get(q["topic"], q["topic"])
    return json.dumps(public, ensure_ascii=False)


def grade_exercise(student_answer: str, exercise_id: str | None = None) -> str:
    """
    判分 active exercise。
      - 选择题:大小写无关地匹配选项字母
      - 填空/计算:数值容差 ±2%(若可解析为数字),否则字符串归一化匹配
    """
    profile = _load_profile()
    if not ACTIVE_EXERCISE_PATH.exists():
        return json.dumps({"error": "当前没有正在进行的题目,请先调用 generate_exercise"}, ensure_ascii=False)
    q = json.loads(ACTIVE_EXERCISE_PATH.read_text(encoding="utf-8"))
    if exercise_id and exercise_id != q["id"]:
        return json.dumps({"error": f"传入的 exercise_id={exercise_id} 与当前题不一致 ({q['id']})"}, ensure_ascii=False)

    correct_answer = str(q["answer"]).strip()
    given = str(student_answer).strip()

    # 数值题尝试数值比较
    def _try_float(s: str) -> float | None:
        s = s.replace(",", "").replace(" ", "").rstrip("%")
        try:
            return float(s)
        except ValueError:
            return None

    is_correct = False
    if q["type"] == "single_choice":
        # 取首字母 A/B/C/D
        m1 = re.search(r"[ABCDabcd]", given)
        m2 = re.search(r"[ABCDabcd]", correct_answer)
        if m1 and m2:
            is_correct = m1.group(0).upper() == m2.group(0).upper()
    else:
        x, y = _try_float(given), _try_float(correct_answer)
        if x is not None and y is not None:
            tol = max(abs(y) * 0.02, 1e-3)
            is_correct = abs(x - y) <= tol
        else:
            is_correct = given.replace(" ", "").lower() == correct_answer.replace(" ", "").lower()

    # 写入历史
    topic = q["topic"]
    profile.setdefault("topic_stats", {}).setdefault(topic, {"asked": 0, "attempted": 0, "correct": 0, "wrong": 0})
    profile["topic_stats"][topic]["attempted"] += 1
    if is_correct:
        profile["topic_stats"][topic]["correct"] += 1
    else:
        profile["topic_stats"][topic]["wrong"] += 1
        profile["wrong_answers"].append({
            "ts": int(time.time()),
            "exercise_id": q["id"],
            "topic": topic,
            "stem": q["stem"],
            "your_answer": given,
            "correct_answer": correct_answer,
            "explanation": q.get("explanation", ""),
        })
    profile["exercise_history"].append({
        "ts": int(time.time()),
        "exercise_id": q["id"],
        "topic": topic,
        "correct": is_correct,
    })
    _save_profile(profile)

    return json.dumps(
        {"is_correct": is_correct,
         "exercise_id": q["id"],
         "topic": topic,
         "topic_name": TOPIC_NAMES.get(topic, topic),
         "correct_answer": correct_answer,
         "your_answer": given,
         "explanation": q.get("explanation", "")},
        ensure_ascii=False,
    )


# ---------- 6. 学习计划生成 ----------
def make_study_plan(days: int = 7,
                    hours_per_day: float = 2.0,
                    goal: str = "期末考试") -> str:
    """
    根据当前学习画像和给定时间预算,生成阶段性复习计划。
    优先安排错题/薄弱章节,然后补全其他章节。
    """
    profile = _load_profile()

    # 各章节优先级:错题数 + (1 - 准确率)*10 + 0.1
    priorities = []
    for t, name in TOPIC_NAMES.items():
        stats = profile["topic_stats"].get(t, {"asked": 0, "attempted": 0, "correct": 0, "wrong": 0})
        attempted = stats["attempted"]
        if attempted > 0:
            acc = stats["correct"] / attempted
            score = stats["wrong"] * 2 + (1 - acc) * 5 + 0.1
        else:
            score = 1.0
        priorities.append((score, t, name, stats))
    priorities.sort(reverse=True)

    total_hours = days * hours_per_day
    # 按优先级权重分配学时
    weights = np.array([p[0] for p in priorities], dtype=float)
    weights = weights / weights.sum()
    hours_alloc = (weights * total_hours).round(1)

    # 切成 days 天的日程
    plan = []
    flat_tasks = []
    for (score, t, name, stats), h in zip(priorities, hours_alloc):
        flat_tasks.append({"topic": t, "name": name, "hours": float(h)})

    cursor = 0
    for d in range(1, days + 1):
        day_budget = hours_per_day
        day_items = []
        while day_budget > 0.05 and cursor < len(flat_tasks):
            task = flat_tasks[cursor]
            if task["hours"] <= 0.05:
                cursor += 1
                continue
            use = min(day_budget, task["hours"])
            day_items.append({
                "topic_name": task["name"],
                "hours": round(use, 2),
                "actions": _suggest_actions(task["topic"]),
            })
            task["hours"] -= use
            day_budget -= use
            if task["hours"] <= 0.05:
                cursor += 1
        plan.append({"day": d, "items": day_items})

    return json.dumps(
        {"goal": goal, "days": days, "hours_per_day": hours_per_day,
         "total_hours": total_hours, "plan": plan,
         "weakest_topics_first": [p[2] for p in priorities[:3]]},
        ensure_ascii=False,
    )


def _suggest_actions(topic: str) -> list[str]:
    base = {
        "ch1_modeling":     ["复习模型分类与现金流要素",      "对比 zero-coupon、annuity 等工具的现金流图"],
        "ch2_interest":     ["熟练 i, i^(p), d, δ 互换公式", "做 3 道复利与利率力换算题"],
        "ch3_annuities":    ["背 a_n、s_n、ä_n、ā_n 公式",   "用 calc_annuity 工具做 2 道现值/累积值题"],
        "ch4_loan":         ["手动写一份还款表",             "用 calc_loan_payment 验证等额还款"],
        "ch5_appraisal":    ["练习 NPV/IRR 计算",          "理解贴现回收期 vs 简单回收期"],
        "ch6_bonds":        ["熟练溢价/折价判断与债券定价",  "做含资本利得税的题目"],
        "ch7_term":         ["现货-远期利率换算",           "Macaulay/修正久期/凸度计算 + 免疫三条件"],
        "ch8_expectations": ["理解理性预期的两个条件",      "结合有效市场假说的实例"],
    }
    return base.get(topic, ["阅读对应章节,做 2 道练习题"])


# ==================================================================
# 工具注册表 + JSON Schema
# ==================================================================
TOOLS_IMPL: dict[str, Callable[..., str]] = {
    "calc_eval":               calc_eval,
    "calc_compound":           calc_compound,
    "calc_present_value":      calc_present_value,
    "calc_annuity":            calc_annuity,
    "calc_loan_payment":       calc_loan_payment,
    "calc_npv":                calc_npv,
    "calc_irr":                calc_irr,
    "calc_bond_price":         calc_bond_price,
    "calc_duration":           calc_duration,
    "calc_force_of_interest":  calc_force_of_interest,
    "calc_nominal_to_effective": calc_nominal_to_effective,
    "search_knowledge":        search_knowledge,
    "log_question":            log_question,
    "get_learning_profile":    get_learning_profile,
    "generate_exercise":       generate_exercise,
    "grade_exercise":          grade_exercise,
    "make_study_plan":         make_study_plan,
}

TOOLS: list[dict] = [
    {
        "type": "function",
        "function": {
            "name": "calc_eval",
            "description": "安全的通用数学表达式计算器,支持 +-*/、**、math.sqrt/log/exp 等。当公式较短可直接代值时使用。",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string", "description": "要计算的数学表达式,如 '1000*(1.05)**10'"}},
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_compound",
            "description": "计算复利累积值 FV。compounding 可选 annual/semiannual/quarterly/monthly/continuous。",
            "parameters": {
                "type": "object",
                "properties": {
                    "principal": {"type": "number"},
                    "rate": {"type": "number", "description": "年利率,小数形式(如 0.05 表示 5%)"},
                    "years": {"type": "number"},
                    "compounding": {"type": "string", "enum": ["annual", "semiannual", "quarterly", "monthly", "weekly", "daily", "continuous"]},
                },
                "required": ["principal", "rate", "years"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_present_value",
            "description": "计算现值 PV。",
            "parameters": {
                "type": "object",
                "properties": {
                    "future_value": {"type": "number"},
                    "rate": {"type": "number"},
                    "years": {"type": "number"},
                    "compounding": {"type": "string", "enum": ["annual", "semiannual", "quarterly", "monthly", "continuous"]},
                },
                "required": ["future_value", "rate", "years"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_annuity",
            "description": "计算等额年金的现值与累积值,返回 a_n 和 s_n。kind ∈ {ordinary(期末), due(期初)}。",
            "parameters": {
                "type": "object",
                "properties": {
                    "payment":  {"type": "number"},
                    "rate":     {"type": "number"},
                    "periods":  {"type": "integer"},
                    "kind":     {"type": "string", "enum": ["ordinary", "due"]},
                },
                "required": ["payment", "rate", "periods"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_loan_payment",
            "description": "计算等额还款贷款的每期还款额,并返回前 12 期还款表。",
            "parameters": {
                "type": "object",
                "properties": {
                    "principal": {"type": "number"},
                    "rate": {"type": "number"},
                    "periods": {"type": "integer"},
                },
                "required": ["principal", "rate", "periods"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_npv",
            "description": "计算 NPV(净现值)。cashflows[k] 表示第 k 期现金流,k 从 0 开始。",
            "parameters": {
                "type": "object",
                "properties": {
                    "rate": {"type": "number"},
                    "cashflows": {"type": "array", "items": {"type": "number"}},
                },
                "required": ["rate", "cashflows"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_irr",
            "description": "求 IRR(使 NPV=0 的折现率)。",
            "parameters": {
                "type": "object",
                "properties": {
                    "cashflows": {"type": "array", "items": {"type": "number"}},
                    "guess":     {"type": "number"},
                },
                "required": ["cashflows"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_bond_price",
            "description": "债券定价。frequency 是每年付息次数(1=年付,2=半年付)。",
            "parameters": {
                "type": "object",
                "properties": {
                    "face_value":   {"type": "number"},
                    "coupon_rate":  {"type": "number", "description": "年票面利率,小数"},
                    "yield_rate":   {"type": "number", "description": "年到期收益率,小数"},
                    "periods":      {"type": "integer", "description": "剩余年数"},
                    "frequency":    {"type": "integer"},
                },
                "required": ["face_value", "coupon_rate", "yield_rate", "periods"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_duration",
            "description": "计算 Macaulay 久期、修正久期、凸度。cashflows 与 times 长度需一致。",
            "parameters": {
                "type": "object",
                "properties": {
                    "cashflows": {"type": "array", "items": {"type": "number"}},
                    "times":     {"type": "array", "items": {"type": "number"}},
                    "yield_rate": {"type": "number"},
                },
                "required": ["cashflows", "times", "yield_rate"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_force_of_interest",
            "description": "由实际年利率 i 计算利率力 δ、贴现率 d 和贴现因子 v。",
            "parameters": {
                "type": "object",
                "properties": {"rate": {"type": "number"}},
                "required": ["rate"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calc_nominal_to_effective",
            "description": "把名义利率 i^(p) 换算为实际年利率 i。",
            "parameters": {
                "type": "object",
                "properties": {
                    "nominal": {"type": "number"},
                    "p": {"type": "integer"},
                },
                "required": ["nominal", "p"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_knowledge",
            "description": "从课程讲义(《Financial Mathematics》)中检索与查询最相关的若干文本片段。涉及定义、概念、章节内容时优先调用。",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "top_k": {"type": "integer"},
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "log_question",
            "description": "记录学生的一次提问到学习画像中(后台调用,不必告知学生)。",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_learning_profile",
            "description": "读取当前学生的学习画像:各章节练习正确率、薄弱章节、最近错题、最近提问等。",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "generate_exercise",
            "description": "从题库中挑一道题。topic 不填则自动选薄弱章节;qtype 可选 single_choice/fill_blank/calculation。",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "enum": list(TOPIC_NAMES.keys())},
                    "qtype": {"type": "string", "enum": ["single_choice", "fill_blank", "calculation"]},
                    "difficulty": {"type": "string"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "grade_exercise",
            "description": "对学生提交的答案进行判分,并把结果写入学习画像。须在 generate_exercise 之后调用。",
            "parameters": {
                "type": "object",
                "properties": {
                    "student_answer": {"type": "string"},
                    "exercise_id": {"type": "string"},
                },
                "required": ["student_answer"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "make_study_plan",
            "description": "根据当前学习画像、目标与时间预算,生成阶段性复习计划。",
            "parameters": {
                "type": "object",
                "properties": {
                    "days": {"type": "integer"},
                    "hours_per_day": {"type": "number"},
                    "goal": {"type": "string"},
                },
            },
        },
    },
]


# ==================================================================
# Agent 主循环 (实验一核心)
# ==================================================================
def build_rag_system_prompt(messages: list[dict]) -> str:
    """把最新一次用户提问的 RAG 检索结果拼到 system prompt 中。"""
    if RAG_LIBRARY is None:
        return SYSTEM_PROMPT

    latest_query = ""
    for m in reversed(messages):
        if m.get("role") == "user":
            latest_query = str(m.get("content", ""))
            break
    if not latest_query.strip():
        return SYSTEM_PROMPT

    context = RAG_LIBRARY.build_context(
        latest_query, top_k=RAG_TOP_K, min_score=RAG_MIN_SCORE
    )
    if not context.strip():
        return SYSTEM_PROMPT

    return (
        f"{SYSTEM_PROMPT}\n\n"
        "以下是从课程讲义检索到的参考资料(context),请优先基于这些内容回答,"
        "并在引用具体定义/公式时简要标注【来源】:\n"
        f"{context}"
    )


def agent_loop(client: OpenAI, messages: list[dict],
               on_tool_call: Callable[[str, dict, str], None] | None = None,
               on_assistant_text: Callable[[str], None] | None = None,
               max_iters: int = 8) -> str:
    """
    Agent 主循环:
      1. 调用模型 (注入 RAG context 到 system message)
      2. 若有 tool_calls,逐个执行并把结果作为 role="tool" 追加
      3. 若没有 tool_calls,把最终答复写回 messages 并 break
    返回最后一条 assistant 文本。
    """
    system_msg = {"role": "system", "content": build_rag_system_prompt(messages)}

    final_text = ""
    for _ in range(max_iters):
        response = client.chat.completions.create(
            model=CHAT_MODEL,
            messages=[system_msg] + messages,
            tools=TOOLS,
            tool_choice="auto",
        )
        message = response.choices[0].message
        tool_calls = getattr(message, "tool_calls", None) or []

        # 把 assistant 这一轮(可能含 tool_calls)写进历史
        assistant_entry: dict = {
            "role": "assistant",
            "content": message.content or "",
        }
        if tool_calls:
            assistant_entry["tool_calls"] = [
                {
                    "id": c.id,
                    "type": "function",
                    "function": {
                        "name": c.function.name,
                        "arguments": c.function.arguments or "{}",
                    },
                }
                for c in tool_calls
            ]
        messages.append(assistant_entry)

        # 没有工具调用 -> 终止
        if not tool_calls:
            final_text = message.content or ""
            if on_assistant_text and final_text:
                on_assistant_text(final_text)
            break

        # 执行每个工具调用
        for call in tool_calls:
            tool_name = call.function.name
            try:
                args = json.loads(call.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}

            fn = TOOLS_IMPL.get(tool_name)
            if fn is None:
                output = f"[error] 未知工具: {tool_name}"
            else:
                try:
                    output = fn(**args)
                except TypeError as e:
                    output = f"[error] 工具参数不匹配: {e}"
                except Exception as e:  # noqa: BLE001
                    output = f"[error] 工具执行异常: {e}"

            if on_tool_call:
                try:
                    on_tool_call(tool_name, args, output)
                except Exception:  # noqa: BLE001
                    pass

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": output,
            })

    return final_text


# ==================================================================
# 命令行入口(便于在终端测试)
# ==================================================================
def main_cli() -> None:
    global RAG_LIBRARY
    client = make_client()
    RAG_LIBRARY = load_or_build_rag_library(
        client=client,
        embedding_model=EMBED_MODEL,
        docs_dir=LIBRARY_DIR,
        index_path=LIBRARY_DIR / "index.npz",
    )
    history: list[dict] = []
    print("【金融数学智能学伴】输入 q/exit 退出。")
    while True:
        try:
            q = input("\033[36m你 >> \033[0m")
        except (EOFError, KeyboardInterrupt):
            break
        if q.strip().lower() in {"q", "exit", ""}:
            break
        log_question(q)
        history.append({"role": "user", "content": q})

        def on_call(name, args, out):
            print(f"\033[33m[Tool] {name}({args}) -> {out[:200]}\033[0m")

        text = agent_loop(client, history, on_tool_call=on_call)
        print(f"\033[32m助手 >>\033[0m {text}\n")


if __name__ == "__main__":
    main_cli()
