"""rag_library.py - 检索增强生成(RAG)知识库实现

完成实验二:实现文本切分、向量化、相似度检索、上下文构建。
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from openai import OpenAI


@dataclass
class Chunk:
    """知识库中的一个文本分块"""
    content: str   # 文本内容
    source: str    # 来源文件名
    index: int     # 在知识库中的序号


class RAGLibrary:
    """
    最小可运行的 RAG 实现:
      1. load_documents:从目录读取 txt/md 文件并切分
      2. _split_text:基于分隔符优先级 + 滑动窗口 的文本切分(进阶任务2)
      3. create_embeddings:批量调用 embedding 接口(每批 <=10)
      4. save_index / load_index:磁盘缓存
      5. _cosine_similarity:余弦相似度
      6. search:返回 top_k 最相关 chunk
      7. build_context:把 top_k chunks 拼接为上下文文本
    """

    def __init__(
        self,
        client: OpenAI,
        embedding_model: str,
        chunk_size: int = 500,
        chunk_overlap: int = 100,
    ) -> None:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        if chunk_overlap < 0 or chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be >= 0 and < chunk_size")

        self.client = client
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.embedding_model = embedding_model

        self.chunks: list[Chunk] = []
        self.embeddings: np.ndarray | None = None

    # ------------------------------------------------------------------
    # 1. 文档读取与切分
    # ------------------------------------------------------------------
    def load_documents(self, dir_path: str | Path) -> None:
        """从目录读取 txt/md 文档,并切分成 chunks。"""
        dir_path = Path(dir_path)
        if not dir_path.is_dir():
            raise NotADirectoryError(f"Not a directory: {dir_path}")

        # 重新加载文档时,先清空旧数据。
        self.chunks = []
        self.embeddings = None

        for path in sorted(dir_path.rglob("*")):
            if path.suffix.lower() not in {".txt", ".md"}:
                continue

            content = path.read_text(encoding="utf-8")
            for text in self._split_text(content):
                self.chunks.append(
                    Chunk(
                        content=text,
                        source=path.name,
                        index=len(self.chunks),
                    )
                )

    def _split_text(self, text: str) -> list[str]:
        """
        基于分隔符优先级 + 滑动窗口的混合切分(实验二进阶任务2):
          1. 先按段落(\n\n) 拆分,逐段累加到 buffer。
          2. 若加入后超出 chunk_size,则 flush buffer 为一个 chunk。
          3. 单段过长时,继续按句子(。.!?!?\n) 细分;再不够则按字符滑窗。
          4. 维护 chunk_overlap:flush 后保留尾部 overlap 字符作为下一个 chunk 起点。
        """
        text = text.strip()
        if not text:
            return []

        chunks: list[str] = []
        buffer = ""

        def flush_buffer() -> None:
            """把当前 buffer 落盘为一个 chunk,并保留尾部 overlap。"""
            nonlocal buffer
            if not buffer.strip():
                buffer = ""
                return
            chunks.append(buffer.strip())
            # 保留尾部 overlap 字符作为下一个 chunk 的起点
            if self.chunk_overlap > 0:
                buffer = buffer[-self.chunk_overlap:]
            else:
                buffer = ""

        # 按多级分隔符拆分:段落 -> 换行 -> 句子 -> 字符
        # rglob:把 text 拆成"片段"序列
        paragraphs = re.split(r"\n\s*\n+", text)

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            if len(para) > self.chunk_size:
                # 段落本身过长,先 flush buffer,再细分这个段落
                flush_buffer()
                for sub in self._split_long_paragraph(para):
                    if len(buffer) + len(sub) + 1 > self.chunk_size and buffer.strip():
                        flush_buffer()
                    if buffer:
                        buffer += "\n" + sub
                    else:
                        buffer = sub
                    if len(buffer) >= self.chunk_size:
                        flush_buffer()
            else:
                # 段落不超长,尝试加入 buffer
                if len(buffer) + len(para) + 2 > self.chunk_size and buffer.strip():
                    flush_buffer()
                if buffer:
                    buffer += "\n\n" + para
                else:
                    buffer = para

        flush_buffer()

        # 去重 + 过滤空块
        seen = set()
        result = []
        for c in chunks:
            c = c.strip()
            if not c or c in seen:
                continue
            seen.add(c)
            result.append(c)
        return result

    def _split_long_paragraph(self, para: str) -> list[str]:
        """对单个超长段落,按句子/单行/字符多级拆分。"""
        # 先按句末标点拆
        sentences = re.split(r"(?<=[。.!?！？])\s+|\n", para)
        sentences = [s.strip() for s in sentences if s.strip()]

        out: list[str] = []
        for s in sentences:
            if len(s) <= self.chunk_size:
                out.append(s)
            else:
                # 退化为字符滑窗
                step = max(1, self.chunk_size - self.chunk_overlap)
                for i in range(0, len(s), step):
                    out.append(s[i : i + self.chunk_size])
        return out

    # ------------------------------------------------------------------
    # 2. embedding 生成 / 保存 / 加载
    # ------------------------------------------------------------------
    def create_embeddings(self, batch_size: int = 10) -> None:
        """
        为所有 chunk 生成 embedding 向量。
        Qwen 的 embedding 接口一次最多 10 条,所以分批调用。
        """
        if not self.chunks:
            raise ValueError("No chunks loaded. Call load_documents() first.")

        texts = [c.content for c in self.chunks]
        vectors: list[list[float]] = []

        for start in range(0, len(texts), batch_size):
            batch = texts[start : start + batch_size]
            response = self.client.embeddings.create(
                model=self.embedding_model,
                input=batch,
            )
            vectors.extend(item.embedding for item in response.data)

        self.embeddings = np.array(vectors, dtype=np.float32)

    def save_index(self, filepath: str | Path) -> None:
        """把 chunks 和 embeddings 保存到本地 npz 文件。"""
        if self.embeddings is None:
            raise ValueError("No embeddings found. Call create_embeddings() first.")

        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        np.savez(
            filepath,
            embeddings=self.embeddings,
            chunks_content=np.array([c.content for c in self.chunks]),
            chunks_source=np.array([c.source for c in self.chunks]),
            chunks_index=np.array([c.index for c in self.chunks]),
        )

    def load_index(self, filepath: str | Path) -> None:
        """从本地 npz 文件加载 chunks 和 embeddings。"""
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"Index file not found: {filepath}")

        data = np.load(filepath, allow_pickle=False)
        self.embeddings = data["embeddings"]
        self.chunks = [
            Chunk(
                content=str(data["chunks_content"][i]),
                source=str(data["chunks_source"][i]),
                index=int(data["chunks_index"][i]),
            )
            for i in range(len(data["chunks_content"]))
        ]

    # ------------------------------------------------------------------
    # 3. 相似度检索
    # ------------------------------------------------------------------
    @staticmethod
    def _cosine_similarity(query: np.ndarray, documents: np.ndarray) -> np.ndarray:
        """
        计算 query 与 documents 中每个向量的余弦相似度。
            cos(a, b) = (a · b) / (||a|| * ||b||)
        """
        query = query.astype(np.float32).reshape(-1)              # (d,)
        docs = documents.astype(np.float32)                       # (n, d)

        q_norm = np.linalg.norm(query) + 1e-12
        d_norm = np.linalg.norm(docs, axis=1) + 1e-12             # (n,)
        return (docs @ query) / (d_norm * q_norm)                 # (n,)

    def _embed_query(self, query: str) -> np.ndarray:
        """单条查询 -> 单条 embedding 向量。"""
        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=[query],
        )
        return np.array(response.data[0].embedding, dtype=np.float32)

    def search(self, query: str, top_k: int = 5) -> list[tuple[Chunk, float]]:
        """返回与 query 最相似的 top_k 个 chunk。"""
        if self.embeddings is None:
            raise ValueError("No embeddings found. Call create_embeddings() first.")
        if top_k <= 0:
            return []

        # 1. 把 query 转为 embedding
        q_vec = self._embed_query(query)

        # 2. 计算与每个 chunk 的余弦相似度
        sims = self._cosine_similarity(q_vec, self.embeddings)

        # 3. 取 top_k
        top_indices = np.argsort(sims)[::-1][:top_k]
        return [(self.chunks[i], float(sims[i])) for i in top_indices]

    # ------------------------------------------------------------------
    # 4. 给 Agent 用的接口:把检索结果拼接成 context 字符串
    # ------------------------------------------------------------------
    def build_context(self, query: str, top_k: int = 5, min_score: float = 0.2) -> str:
        """
        检索 top_k 并拼接成可直接注入 prompt 的字符串,过滤掉相似度过低的结果。
        """
        results = self.search(query, top_k=top_k)
        pieces: list[str] = []
        for chunk, score in results:
            if score < min_score:
                continue
            pieces.append(
                f"【来源:{chunk.source} #{chunk.index} 相似度:{score:.3f}】\n{chunk.content}"
            )
        return "\n\n---\n\n".join(pieces)


# ----------------------------------------------------------------------
# 辅助函数:加载或构建知识库
# ----------------------------------------------------------------------
def load_or_build_rag_library(
    client: OpenAI,
    embedding_model: str = "text-embedding-v4",
    docs_dir: str | Path = "library",
    index_path: str | Path = "library/index.npz",
    verbose: bool = True,
) -> RAGLibrary:
    """优先加载磁盘上已存在的索引;否则从文档构建并保存。"""
    docs_dir = Path(docs_dir)
    index_path = Path(index_path)

    rag = RAGLibrary(client=client, embedding_model=embedding_model)

    if index_path.exists():
        if verbose:
            print(f"[RAG] 加载索引: {index_path}")
        rag.load_index(index_path)
    else:
        if verbose:
            print(f"[RAG] 未找到索引,开始构建: {index_path}")
        rag.load_documents(docs_dir)
        if verbose:
            print(f"[RAG] 共切分出 {len(rag.chunks)} 个文本块,正在生成 embedding ...")
        rag.create_embeddings()
        rag.save_index(index_path)
        if verbose:
            print(f"[RAG] 索引构建完成: {index_path}")

    return rag
