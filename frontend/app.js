/* =====================================================
 * Quanta Tutor 前端逻辑
 * ===================================================== */

// ---------------- Marked & KaTeX 配置 ----------------
const md = window.marked;
md.use({
  breaks: false,
  gfm: true,
});

function renderMarkdown(text) {
  // 把单美元的 inline math 临时占位再 marked,防止下划线被解释
  const placeholders = [];
  let prep = text.replace(/\$\$([\s\S]+?)\$\$/g, (_, m) => {
    placeholders.push({ block: true, expr: m });
    return `@@MATHBLOCK${placeholders.length - 1}@@`;
  });
  prep = prep.replace(/\$([^$\n]+?)\$/g, (_, m) => {
    placeholders.push({ block: false, expr: m });
    return `@@MATHINLINE${placeholders.length - 1}@@`;
  });
  let html = md.parse(prep);
  html = html.replace(/@@MATHBLOCK(\d+)@@/g, (_, i) => {
    const p = placeholders[+i];
    try {
      return katex.renderToString(p.expr, { displayMode: true, throwOnError: false });
    } catch { return `<code>$$${p.expr}$$</code>`; }
  });
  html = html.replace(/@@MATHINLINE(\d+)@@/g, (_, i) => {
    const p = placeholders[+i];
    try {
      return katex.renderToString(p.expr, { displayMode: false, throwOnError: false });
    } catch { return `<code>$${p.expr}$</code>`; }
  });
  return html;
}

// ---------------- DOM Refs ----------------
const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

const messagesEl = $("#messages");
const inputEl    = $("#input");
const composer   = $("#composer");
const resetBtn   = $("#reset-chat");

// ---------------- Tab 切换 ----------------
$$(".tab").forEach(btn => {
  btn.addEventListener("click", () => {
    const target = btn.dataset.pane;
    $$(".tab").forEach(b => b.classList.toggle("active", b === btn));
    $$(".pane").forEach(p => p.classList.toggle("active", p.id === `pane-${target}`));
    if (target === "profile") refreshProfile();
    if (target === "exercise") loadTopicsInto("#ex-topic");
  });
});

// ---------------- Edition Number ----------------
{
  const today = new Date();
  const num = today.getFullYear().toString().slice(-2) +
              String(today.getMonth() + 1).padStart(2, "0") +
              String(today.getDate()).padStart(2, "0");
  $("#today-num").textContent = num;
}

// ---------------- 快速提问按钮 ----------------
$$(".qbtn").forEach(b => {
  b.addEventListener("click", () => {
    inputEl.value = b.dataset.q;
    inputEl.focus();
  });
});

// ---------------- 消息渲染 ----------------
function appendMessage(role, body, opts = {}) {
  const article = document.createElement("article");
  article.className = `msg msg-${role}`;
  article.innerHTML = `
    <div class="msg-bubble">
      <div class="msg-meta">${roleLabel(role)}</div>
      <div class="msg-body"></div>
    </div>
  `;
  if (typeof body === "string") {
    article.querySelector(".msg-body").innerHTML = body;
  } else if (body instanceof Node) {
    article.querySelector(".msg-body").appendChild(body);
  }
  messagesEl.appendChild(article);
  scrollToBottom();
  return article;
}
function roleLabel(role) {
  return ({
    user: "你",
    assistant: "助教",
    system: "系统",
  })[role] || role;
}
function scrollToBottom() {
  // 滚动 chat-scroll 容器,而非整个页面
  const scroller = document.getElementById("chat-scroll");
  if (scroller) {
    scroller.scrollTo({ top: scroller.scrollHeight, behavior: "smooth" });
  }
}

// ---------------- Chat 提交 ----------------
let isStreaming = false;
composer.addEventListener("submit", async e => {
  e.preventDefault();
  if (isStreaming) return;
  const text = inputEl.value.trim();
  if (!text) return;
  await sendMessage(text);
});

inputEl.addEventListener("keydown", e => {
  if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
    composer.requestSubmit();
  }
});

resetBtn.addEventListener("click", async () => {
  if (!confirm("清空当前对话?(学情数据保留)")) return;
  messagesEl.innerHTML = "";
  appendMessage("system", `<p class="hint">对话已重置。</p>`);
  // 让下一次 chat 的请求带 reset=true
  pendingReset = true;
});

let pendingReset = false;

async function sendMessage(text) {
  // 1. 渲染用户消息
  const userArticle = appendMessage("user", "");
  userArticle.querySelector(".msg-body").innerHTML = renderMarkdown(text);
  if (window.renderMathInElement) {
    window.renderMathInElement(userArticle, mathDelimiters());
  }
  inputEl.value = "";
  inputEl.style.height = "auto";

  // 2. 创建助教占位消息
  const assistant = appendMessage("assistant", "");
  const body = assistant.querySelector(".msg-body");
  const traceContainer = document.createElement("div");
  traceContainer.className = "tool-traces";
  body.appendChild(traceContainer);
  const typing = document.createElement("div");
  typing.className = "typing";
  typing.innerHTML = `<span class="dot"></span><span class="dot"></span><span class="dot"></span><span style="margin-left:8px">思考中…</span>`;
  body.appendChild(typing);

  isStreaming = true;
  setComposerEnabled(false);

  try {
    const resp = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text, reset: pendingReset }),
    });
    pendingReset = false;
    if (!resp.ok || !resp.body) throw new Error("请求失败 " + resp.status);

    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    let answerHtml = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      const events = buffer.split("\n\n");
      buffer = events.pop();

      for (const raw of events) {
        if (!raw.trim()) continue;
        const evMatch = /^event:\s*(.+)$/m.exec(raw);
        const dataMatch = /^data:\s*([\s\S]+)$/m.exec(raw);
        if (!evMatch || !dataMatch) continue;
        const ev = evMatch[1].trim();
        let payload = dataMatch[1].trim();
        try { payload = JSON.parse(payload); } catch {}

        if (ev === "tool") {
          const card = renderToolCard(payload);
          // 把 typing 始终放在最末尾
          traceContainer.appendChild(card);
          if (typing.parentNode === body) body.removeChild(typing);
          body.appendChild(typing);
          scrollToBottom();
        } else if (ev === "answer") {
          answerHtml = renderMarkdown(payload.text || "");
          const ansEl = document.createElement("div");
          ansEl.className = "final-answer";
          ansEl.innerHTML = answerHtml;
          // 替换 typing 为答案
          if (typing.parentNode === body) body.removeChild(typing);
          // 清掉旧答案(若多次回答)
          $$(".final-answer", body).forEach(n => n.remove());
          body.appendChild(ansEl);
          if (window.renderMathInElement) {
            window.renderMathInElement(ansEl, mathDelimiters());
          }
          scrollToBottom();
        } else if (ev === "error") {
          if (typing.parentNode === body) body.removeChild(typing);
          const errEl = document.createElement("div");
          errEl.className = "ex-result wrong show";
          errEl.innerHTML = `<div class="verdict">⚠ 出错了</div><div>${escapeHtml(payload.message || "")}</div>`;
          body.appendChild(errEl);
        } else if (ev === "done") {
          if (typing.parentNode === body) body.removeChild(typing);
        }
      }
    }
  } catch (err) {
    const errEl = document.createElement("div");
    errEl.className = "ex-result wrong show";
    errEl.innerHTML = `<div class="verdict">⚠ 网络错误</div><div>${escapeHtml(err.message)}</div>`;
    body.appendChild(errEl);
  } finally {
    isStreaming = false;
    setComposerEnabled(true);
    if (typing.parentNode === body) body.removeChild(typing);
  }
}

function renderToolCard({ name, arguments: args, output }) {
  const wrap = document.createElement("div");
  wrap.className = "tool-trace";
  let preview = "";
  // 简短预览
  if (typeof output === "string" && output.length > 0) {
    if (output.startsWith("{") || output.startsWith("[")) {
      preview = output.slice(0, 100) + (output.length > 100 ? "…" : "");
    } else {
      preview = output.slice(0, 80) + (output.length > 80 ? "…" : "");
    }
  }
  wrap.innerHTML = `
    <div class="tool-head">
      <span class="tool-icon">⚙︎</span>
      <span class="tool-name">${escapeHtml(name)}</span>
      <span style="opacity:0.6;font-size:11px;">${escapeHtml(preview)}</span>
      <span class="tool-toggle">▸</span>
    </div>
    <div class="tool-body">
      <div class="lbl">arguments</div>
      <pre>${escapeHtml(JSON.stringify(args, null, 2))}</pre>
      <div class="lbl">output</div>
      <pre>${escapeHtml(prettyOutput(output))}</pre>
    </div>
  `;
  wrap.querySelector(".tool-head").addEventListener("click", () => {
    wrap.classList.toggle("open");
  });
  return wrap;
}

function prettyOutput(s) {
  if (typeof s !== "string") return JSON.stringify(s, null, 2);
  try {
    return JSON.stringify(JSON.parse(s), null, 2);
  } catch {
    return s;
  }
}

function setComposerEnabled(yes) {
  inputEl.disabled = !yes;
  $(".send-btn", composer).disabled = !yes;
}

function escapeHtml(s) {
  return String(s ?? "").replace(/[&<>"']/g, c =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
  );
}

function mathDelimiters() {
  return {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$",  right: "$",  display: false },
      { left: "\\[", right: "\\]", display: true },
      { left: "\\(", right: "\\)", display: false },
    ],
    throwOnError: false,
  };
}

// ---------------- 自适应 textarea ----------------
inputEl.addEventListener("input", () => {
  inputEl.style.height = "auto";
  inputEl.style.height = Math.min(inputEl.scrollHeight, 220) + "px";
});


// =====================================================
// PANE 2: 练习
// =====================================================
const exTopicSel = $("#ex-topic");
const exTypeSel  = $("#ex-type");
const exNew      = $("#ex-new");
const exCard     = $("#ex-card");
const exPlace    = $("#ex-placeholder");
const exId       = $("#ex-id");
const exTopicTag = $("#ex-topic-tag");
const exStem     = $("#ex-stem");
const exOptions  = $("#ex-options");
const exAnswer   = $("#ex-answer");
const exSubmit   = $("#ex-submit");
const exResult   = $("#ex-result");

let topicsCache = null;
async function loadTopicsInto(selector) {
  if (!topicsCache) {
    const r = await fetch("/api/topics");
    topicsCache = await r.json();
  }
  const sel = $(selector);
  if (!sel) return;
  if (sel.options.length > 1) return; // 已加载
  for (const t of topicsCache) {
    const opt = document.createElement("option");
    opt.value = t.key;
    opt.textContent = t.name;
    sel.appendChild(opt);
  }
}
loadTopicsInto("#ex-topic");

let currentExercise = null;

exNew.addEventListener("click", async () => {
  exNew.disabled = true;
  exNew.textContent = "加载中…";
  exResult.classList.remove("show", "correct", "wrong");
  exAnswer.value = "";
  try {
    const body = {};
    if (exTopicSel.value) body.topic = exTopicSel.value;
    if (exTypeSel.value)  body.qtype = exTypeSel.value;
    const r = await fetch("/api/exercise", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    const data = await r.json();
    if (data.error) {
      alert(data.error); return;
    }
    currentExercise = data;
    renderExercise(data);
  } catch (e) {
    alert("生成题目失败: " + e.message);
  } finally {
    exNew.disabled = false;
    exNew.innerHTML = `<svg viewBox="0 0 24 24" width="14" height="14"><path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg> 生成题目`;
  }
});

function renderExercise(q) {
  exPlace.hidden = true;
  exCard.hidden = false;
  exId.textContent = `№ ${q.id}`;
  exTopicTag.textContent = q.topic_name || q.topic;
  exStem.innerHTML = renderMarkdown(q.stem);
  if (window.renderMathInElement) window.renderMathInElement(exStem, mathDelimiters());

  exOptions.innerHTML = "";
  if (q.type === "single_choice" && Array.isArray(q.options)) {
    q.options.forEach(opt => {
      const li = document.createElement("li");
      li.innerHTML = renderMarkdown(opt);
      li.addEventListener("click", () => {
        $$("#ex-options li").forEach(x => x.classList.remove("selected"));
        li.classList.add("selected");
        const m = /[ABCD]/i.exec(opt);
        if (m) exAnswer.value = m[0].toUpperCase();
      });
      exOptions.appendChild(li);
    });
  }
  exCard.scrollIntoView({ behavior: "smooth", block: "center" });
}

exSubmit.addEventListener("click", submitAnswer);
exAnswer.addEventListener("keydown", e => {
  if (e.key === "Enter") { e.preventDefault(); submitAnswer(); }
});

async function submitAnswer() {
  if (!currentExercise) { alert("请先生成一道题。"); return; }
  const ans = exAnswer.value.trim();
  if (!ans) { alert("请输入答案。"); return; }
  exSubmit.disabled = true;
  try {
    const r = await fetch("/api/grade", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ student_answer: ans, exercise_id: currentExercise.id }),
    });
    const data = await r.json();
    showResult(data);
  } finally {
    exSubmit.disabled = false;
  }
}

function showResult(data) {
  exResult.className = "ex-result show " + (data.is_correct ? "correct" : "wrong");
  exResult.innerHTML = `
    <div class="verdict">${data.is_correct ? "✓ 正确" : "✗ 答错了"}</div>
    <div class="label-row">你的答案</div>
    <div>${escapeHtml(data.your_answer)}</div>
    <div class="label-row">参考答案</div>
    <div>${escapeHtml(data.correct_answer)}</div>
    <div class="label-row">解析</div>
    <div>${renderMarkdown(data.explanation || "")}</div>
  `;
  if (window.renderMathInElement) window.renderMathInElement(exResult, mathDelimiters());
}


// =====================================================
// PANE 3: 学情
// =====================================================
async function refreshProfile() {
  const r = await fetch("/api/profile");
  const p = await r.json();

  $("#kpi-q").textContent = p.total_questions ?? 0;
  $("#kpi-ex").textContent = p.total_exercises ?? 0;
  $("#kpi-wrong").textContent = p.wrong_count ?? 0;

  let totalAttempt = 0, totalCorrect = 0;
  for (const k in (p.by_topic || {})) {
    totalAttempt += p.by_topic[k].attempted || 0;
    totalCorrect += p.by_topic[k].correct || 0;
  }
  $("#kpi-acc").textContent = totalAttempt > 0
    ? Math.round((totalCorrect / totalAttempt) * 100) + "%"
    : "—";

  // topic grid
  const grid = $("#topic-grid");
  grid.innerHTML = "";
  const weakSet = new Set((p.weakest_topics || []).map(t => t.topic));
  const entries = Object.entries(p.by_topic || {});
  if (entries.length === 0) {
    grid.innerHTML = `<div class="empty-row">尚无数据 — 先问几个问题或做几道题吧。</div>`;
  } else {
    for (const [topic, info] of entries) {
      const card = document.createElement("div");
      card.className = "topic-card" + (weakSet.has(topic) ? " weak" : "");
      const acc = info.accuracy;
      card.innerHTML = `
        <div class="topic-name">${escapeHtml(info.name)}</div>
        <div class="stat-row">
          <span>提问 <strong>${info.asked}</strong></span>
          <span>答题 <strong>${info.attempted}</strong></span>
          <span>错 <strong>${info.wrong}</strong></span>
        </div>
        <div class="acc-bar"><div class="acc-fill" style="width: ${acc != null ? Math.round(acc * 100) : 0}%"></div></div>
        <div class="acc-text">${acc != null ? "正确率 " + Math.round(acc * 100) + "%" : "尚未答题"}</div>
      `;
      grid.appendChild(card);
    }
  }

  // wrong list
  const list = $("#recent-wrong");
  list.innerHTML = "";
  const wrongs = p.recent_wrong || [];
  if (wrongs.length === 0) {
    list.innerHTML = `<div class="empty-row">暂无错题。</div>`;
  } else {
    for (const w of wrongs.slice().reverse()) {
      const item = document.createElement("div");
      item.className = "wrong-item";
      item.innerHTML = `
        <div class="stem">${renderMarkdown(w.stem || "")}</div>
        <div class="answers">
          <span class="yours">你: ${escapeHtml(w.your_answer || "")}</span>
          &nbsp;&nbsp;<span class="truth">正解: ${escapeHtml(w.correct_answer || "")}</span>
        </div>
        <div class="expl">${renderMarkdown(w.explanation || "")}</div>
      `;
      if (window.renderMathInElement) window.renderMathInElement(item, mathDelimiters());
      list.appendChild(item);
    }
  }
}

$("#reset-profile").addEventListener("click", async () => {
  if (!confirm("将清除所有学情数据(提问历史、错题、画像)。确定吗?")) return;
  await fetch("/api/reset", { method: "POST" });
  refreshProfile();
});


// =====================================================
// PANE 4: 规划
// =====================================================
$("#plan-go").addEventListener("click", async () => {
  const days = +$("#plan-days").value || 7;
  const hours = +$("#plan-hours").value || 2;
  const goal = $("#plan-goal").value || "期末冲刺";
  const out = $("#plan-output");
  out.innerHTML = `<div class="placeholder"><div class="ph-icon">⏳</div><p>正在规划...</p></div>`;
  const r = await fetch("/api/plan", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ days, hours_per_day: hours, goal }),
  });
  const data = await r.json();
  renderPlan(data);
});

function renderPlan(data) {
  const out = $("#plan-output");
  out.innerHTML = "";
  const summary = document.createElement("div");
  summary.className = "plan-summary";
  summary.innerHTML = `<strong>目标:</strong> ${escapeHtml(data.goal)}　·　<strong>${data.days} 天</strong> × <strong>${data.hours_per_day} h/天</strong>　·　总计 ${data.total_hours} 小时<br/>
    <span style="color:var(--ink-faint);font-size:14px;">最优先复习: ${(data.weakest_topics_first || []).map(escapeHtml).join("、")}</span>`;
  out.appendChild(summary);

  for (const day of data.plan || []) {
    const card = document.createElement("div");
    card.className = "plan-day";
    const itemsHtml = (day.items || []).map(it => `
      <div class="item">
        <div class="item-title">
          <span>${escapeHtml(it.topic_name)}</span>
          <span class="item-hours">${it.hours} h</span>
        </div>
        <ul class="item-actions">
          ${(it.actions || []).map(a => `<li>${escapeHtml(a)}</li>`).join("")}
        </ul>
      </div>
    `).join("") || `<div style="color:var(--ink-faint);font-style:italic;">休息日 / 补做错题</div>`;
    card.innerHTML = `
      <div>
        <div class="day-num">D${day.day}</div>
        <div class="day-label">Day ${day.day}</div>
      </div>
      <div class="day-items">${itemsHtml}</div>
    `;
    out.appendChild(card);
  }
}
