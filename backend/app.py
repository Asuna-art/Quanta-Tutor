"""app.py - FastAPI Web 服务

提供以下端点:
  GET  /                      返回前端页面
  GET  /static/*              静态资源
  POST /api/chat              提交一次提问,使用 SSE 流式返回工具调用过程与最终回答
  GET  /api/profile           获取学习画像
  POST /api/reset             重置学习画像
  POST /api/exercise          直接生成一道练习题(供前端"练习"标签页用)
  POST /api/grade             直接判分一道练习题
  POST /api/plan              生成学习计划
"""
from __future__ import annotations

import json
import os
import threading
import time
from pathlib import Path
from queue import Queue, Empty
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import (FileResponse, HTMLResponse, JSONResponse,
                               StreamingResponse)
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import agent
from rag_library import load_or_build_rag_library

load_dotenv(override=True)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LIBRARY_DIR = PROJECT_ROOT / "library"
FRONTEND_DIR = PROJECT_ROOT / "frontend"
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

# 全局会话历史(单用户场景,实际部署可按 user_id 隔离)
SESSION_HISTORY: list[dict] = []
SESSION_LOCK = threading.Lock()

app = FastAPI(title="金融数学智能学伴 API")

# ---------- 启动时初始化 RAG ----------
@app.on_event("startup")
def startup() -> None:
    client = agent.make_client()
    agent.RAG_LIBRARY = load_or_build_rag_library(
        client=client,
        embedding_model=agent.EMBED_MODEL,
        docs_dir=LIBRARY_DIR,
        index_path=LIBRARY_DIR / "index.npz",
    )
    app.state.client = client
    print("[startup] RAG 知识库就绪,共", len(agent.RAG_LIBRARY.chunks), "个 chunk")


# ----------------------------------------------------------------
# 静态资源
# ----------------------------------------------------------------
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


@app.get("/", response_class=HTMLResponse)
def index() -> HTMLResponse:
    html = (FRONTEND_DIR / "index.html").read_text(encoding="utf-8")
    return HTMLResponse(html)


# ----------------------------------------------------------------
# 数据模型
# ----------------------------------------------------------------
class ChatRequest(BaseModel):
    message: str
    reset: bool = False


class ExerciseRequest(BaseModel):
    topic: str | None = None
    qtype: str | None = None


class GradeRequest(BaseModel):
    student_answer: str
    exercise_id: str | None = None


class PlanRequest(BaseModel):
    days: int = 7
    hours_per_day: float = 2.0
    goal: str = "期末考试冲刺"


# ----------------------------------------------------------------
# /api/chat —— SSE 流式
# ----------------------------------------------------------------
def _sse(event: str, data: dict | str) -> str:
    payload = data if isinstance(data, str) else json.dumps(data, ensure_ascii=False)
    return f"event: {event}\ndata: {payload}\n\n"


@app.post("/api/chat")
def chat(req: ChatRequest, request: Request):
    if not req.message.strip():
        raise HTTPException(400, "message 不能为空")

    if req.reset:
        with SESSION_LOCK:
            SESSION_HISTORY.clear()

    # 记录提问
    agent.log_question(req.message)
    with SESSION_LOCK:
        SESSION_HISTORY.append({"role": "user", "content": req.message})
        # 拷贝一份用于本次回合,后续把新增条目写回
        history_copy = list(SESSION_HISTORY)

    queue: Queue = Queue()

    def on_tool_call(name: str, args: dict, output: str) -> None:
        queue.put(_sse("tool", {
            "name": name,
            "arguments": args,
            "output": output[:4000],
        }))

    def on_assistant_text(text: str) -> None:
        queue.put(_sse("answer", {"text": text}))

    def worker() -> None:
        try:
            agent.agent_loop(
                request.app.state.client,
                history_copy,
                on_tool_call=on_tool_call,
                on_assistant_text=on_assistant_text,
            )
            # 把新增内容写回会话
            with SESSION_LOCK:
                # history_copy 比 SESSION_HISTORY 长出来的部分,就是本回合新增
                if len(history_copy) > len(SESSION_HISTORY):
                    SESSION_HISTORY.extend(history_copy[len(SESSION_HISTORY):])
            queue.put(_sse("done", {}))
        except Exception as e:  # noqa: BLE001
            queue.put(_sse("error", {"message": str(e)}))
            queue.put(_sse("done", {}))

    threading.Thread(target=worker, daemon=True).start()

    def event_stream():
        while True:
            try:
                item = queue.get(timeout=180)
            except Empty:
                yield _sse("error", {"message": "timeout"})
                break
            yield item
            if item.startswith("event: done"):
                break

    return StreamingResponse(event_stream(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache",
                                      "X-Accel-Buffering": "no"})


# ----------------------------------------------------------------
# /api/profile —— 学习画像
# ----------------------------------------------------------------
@app.get("/api/profile")
def get_profile():
    return JSONResponse(json.loads(agent.get_learning_profile()))


@app.post("/api/reset")
def reset_profile():
    profile_path = DATA_DIR / "learning_profile.json"
    if profile_path.exists():
        profile_path.unlink()
    active = DATA_DIR / "active_exercise.json"
    if active.exists():
        active.unlink()
    with SESSION_LOCK:
        SESSION_HISTORY.clear()
    return {"ok": True}


# ----------------------------------------------------------------
# /api/exercise & /api/grade
# ----------------------------------------------------------------
@app.post("/api/exercise")
def api_exercise(req: ExerciseRequest):
    out = agent.generate_exercise(topic=req.topic, qtype=req.qtype)
    return JSONResponse(json.loads(out))


@app.post("/api/grade")
def api_grade(req: GradeRequest):
    out = agent.grade_exercise(student_answer=req.student_answer,
                               exercise_id=req.exercise_id)
    return JSONResponse(json.loads(out))


# ----------------------------------------------------------------
# /api/plan
# ----------------------------------------------------------------
@app.post("/api/plan")
def api_plan(req: PlanRequest):
    out = agent.make_study_plan(days=req.days,
                                hours_per_day=req.hours_per_day,
                                goal=req.goal)
    return JSONResponse(json.loads(out))


# ----------------------------------------------------------------
# /api/topics —— 章节列表
# ----------------------------------------------------------------
@app.get("/api/topics")
def api_topics():
    return JSONResponse([
        {"key": k, "name": v} for k, v in agent.TOPIC_NAMES.items()
    ])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
