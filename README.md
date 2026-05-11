# 金融数学智能学伴 (Financial Mathematics Tutor)

> 一个面向《金融数学》课程的智能学习助手

---

## 项目简介

本项目以一门具体课程 —— **金融数学 (Financial Mathematics, J2FIN)** —— 为载体，构建了一个能够 **回答问题、检索讲义、诊断学情、生成练习、规划学习路径** 的智能学伴系统。讲义内容覆盖 8 章:利率与现金流建模、年金与价值方程、贷款偿还表、NPV/IRR 投资评估、固定利率证券、利率期限结构 (久期、凸度、免疫)、理性预期理论。

### 一图看懂三个任务的对应关系

| 实验/作业 | 要求 | 项目中对应实现 |
| --- | --- | --- |
| **实验一 必做** | 补全 `agent_loop` | `backend/agent.py` 中的 `agent_loop()` |
| **实验一 进阶 1** | 提供计算器工具 | `calc_eval` + 11 个金融专用计算器 (复利/年金/贷款/NPV/IRR/久期...) |
| **实验二 必做** | 文本切分 + embedding + 余弦相似度 + search | `backend/rag_library.py` (`RAGLibrary`) |
| **实验二 进阶 1** | RAG 工具化 | `search_knowledge` 工具,Agent 可主动检索 |
| **实验二 进阶 2** | 基于分隔符的切分 | `_split_text` 多级分隔符 + buffer + overlap |
| **大作业 (1)** 智能问答 | 结构化回答 | 系统提示词要求 "定义—原理—示例—易错点" 四段式 |
| **大作业 (2)** 知识库 | 接入课程资料 | `library/` 内 9 个 md 文件 (8 章讲义 + 中文速查) |
| **大作业 (3)** 学情诊断 | 识别薄弱知识点 | `get_learning_profile` + 主题分类 + 错题统计 |
| **大作业 (4)** 个性化练习 | 生成 + 评判 + 反馈 | `generate_exercise` + `grade_exercise` (12 题种子题库) |
| **大作业 (5)** 学习计划 | 阶段性复习 | `make_study_plan` 按薄弱章节加权排课 |
| **大作业 (6)** 过程记录 | 短期记忆 | `data/learning_profile.json` 持久化提问/错题 |

---

## 目录结构

```
fm_tutor/
├── library/                       # 金融数学知识库 (9 个 md 文件)
│   ├── ch1_data_and_modeling.md
│   ├── ch2_interest_rates.md
│   ├── ch3_annuities.md
│   ├── ch4_loan_schedules.md
│   ├── ch5_investment_appraisal.md
│   ├── ch6_fixed_interest_securities.md
│   ├── ch7_term_structure.md
│   ├── ch8_rational_expectations.md
│   └── core_concepts_zh.md         # 中文速查 + 公式表
│
├── backend/
│   ├── rag_library.py              # 实验二: 文本切分 / embedding / 余弦相似度 / 检索
│   ├── agent.py                    # 实验一: Agent 主循环 + 17 个工具
│   └── app.py                      # FastAPI 服务 + SSE 流式响应
│
├── frontend/                       # 学术金融报刊风格 Web 界面
│   ├── index.html                  # 4 个 Tab: 问答/练习/学情/规划
│   ├── style.css                   # Fraunces + 思源宋体, 暖象牙底, 琥珀+靛蓝点缀
│   └── app.js                      # SSE 流式渲染 + KaTeX 数学公式 + Markdown
│
├── data/                           # 运行时存储 (自动生成)
│   ├── learning_profile.json       # 学情画像 (提问/错题统计)
│   ├── exercise_bank.json          # 题库 (含种子 12 题)
│   └── active_exercise.json        # 当前活跃题目
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## 快速开始

### 1. 准备 API Key

在 [阿里云百炼平台](https://bailian.console.aliyun.com/) 创建 API Key。

### 2. 安装依赖

```bash
cd fm_tutor
pip install -r requirements.txt
```

### 3. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env, 填入你的 API_KEY
```

### 4. 启动服务

```bash
cd fm_tutor\backend
python app.py
```

首次启动时会自动构建 RAG 索引 (调用 embedding 接口),之后会从 `library/index.npz` 读取缓存,启动 < 2 秒。

### 5. 访问网页

浏览器打开 `http://localhost:8000` 即可使用。

也支持 **命令行模式**:

```bash
cd backend
python agent.py    # 进入终端 REPL
```

---

## 核心功能演示

### 智能问答 (含工具调用 + RAG)

向系统提问 *"年利率 6%、季度复利,本金 1 万元 5 年后变多少?"*,系统会:

1. 自动检索 `library/ch2_interest_rates.md` 中的复利定义注入 system prompt
2. 调用 `calc_compound` 工具计算,前端实时展示工具调用过程
3. 用 "定义→原理→示例→易错点" 结构化输出最终答案
4. 后台记录该提问到 `learning_profile.json`,归类为 `ch2_interest`

### 个性化练习

- 从 12 题种子题库 (覆盖 8 章) 中按 **薄弱章节优先** 抽题
- 支持选择题 / 填空题 / 计算题
- `grade_exercise` 数值题用 ±2% 容差判分,选择题字母匹配

### 学习诊断

页面右侧 KPI:总提问数 / 错题数 / 已练题数 / 薄弱章节数,并以红色高亮标记薄弱章节。

### 学习规划

输入 "目标 + 天数 + 每日小时",系统按 **薄弱权重** 把章节分配到 D1/D2/D3...,生成可执行复习日程。

---

## 技术亮点

### Agent Loop

```python
# backend/agent.py 中的 agent_loop
while iters < max_iters:
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role":"system","content":sys_prompt}] + messages,
        tools=TOOLS,
    )
    msg = response.choices[0].message
    # 1. 没有 tool_calls -> 输出最终答案,break
    # 2. 有 tool_calls -> 解析参数 -> 执行工具 -> role="tool" 回填 -> 继续
```

### RAG 进阶切分 

`_split_text` 实现 **多级分隔符 + buffer + overlap**:段落 → 换行 → 句子 → 字符滑窗。当 buffer 超过 `chunk_size` 时落盘,小片段合并到 buffer,长片段递归用更细分隔符切。

### 流式 UI

后端用 `StreamingResponse` 推送 SSE,事件类型:`tool` / `answer` / `error` / `done`。前端用 `ReadableStream` 解析,**工具调用过程实时渲染为可折叠的 trace 卡片**,数学公式经 KaTeX 渲染。

### 设计语言

刻意避开 "AI slop" 的紫渐变 + 卡片堆叠风格,采用 **学术金融报刊** 美学:暖象牙背景、衬线显示字体 (Fraunces / Cormorant Garamond / Noto Serif SC)、琥珀+靛蓝点缀、四角装饰、kicker + double rule 标题层级。

---

## 工具列表 (Agent 可用的 17 个工具)

| 类别 | 工具 |
| --- | --- |
| 通用计算 | `calc_eval` (安全 eval) |
| 利率/复利 | `calc_compound`, `calc_present_value`, `calc_force_of_interest`, `calc_nominal_to_effective` |
| 年金/贷款 | `calc_annuity`, `calc_loan_payment` |
| 投资评估 | `calc_npv`, `calc_irr` |
| 债券 | `calc_bond_price`, `calc_duration` |
| 知识库 | `search_knowledge` |
| 学情/练习 | `log_question`, `get_learning_profile`, `generate_exercise`, `grade_exercise`, `make_study_plan` |

---

##  扩展指南

### 替换为其他课程

1. 把 `library/` 替换为新课程的 md/txt 资料
2. 删除 `library/index.npz` (会自动重建)
3. 修改 `agent.py` 中的 `TOPIC_KEYWORDS` 和 `TOPIC_NAMES`
4. 修改种子题库 `_exercise_seed_bank()`

### 替换大模型

只需修改 `.env` 中的 `BASE_URL` / `API_KEY` / `CHAT_MODEL` / `EMBED_MODEL`,任何兼容 OpenAI SDK 的模型 (DeepSeek、智谱、Moonshot 等) 都可以。

### 切换为多用户

当前 `SESSION_HISTORY` 是全局单会话。改为 dict-per-user-id 即可支持多用户并发。

---

## 思考题简答 (实验一/二)

> **为什么不直接把所有文档丢给模型?**
> 上下文窗口有限 (qwen-plus ~128K),且每 token 都按计费。检索把 100+ 页讲义压缩到 4~5 个最相关的 chunk,在准确率和成本之间取平衡。

> **embedding 检索 vs rerank?**
> embedding 是双塔模型,query 和 doc 独立编码,**速度快但精度低**;rerank 是 cross-encoder,query 和 doc 联合编码,**精度高但只能用于小批次重排**。生产中通常 embedding 召回 top-50 → rerank 精排 top-5。

> **基于语义的切分?**
> 可以用相邻句子 embedding 余弦相似度判断 "话题边界",相似度骤降处切分。优点是切口对齐语义,缺点是需要预先 embedding,慢且贵。本项目用 "段落→换行→句子" 多级规则切分作为折中。

---

## 许可

仅供课程作业演示使用。讲义版权归原作者所有。
