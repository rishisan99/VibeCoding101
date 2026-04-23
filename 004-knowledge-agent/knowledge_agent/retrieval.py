import re

import numpy as np


def _tokens(text: str) -> set[str]:
    """Basic token set for keyword overlap."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine similarity between vectors."""
    denom = (np.linalg.norm(a) * np.linalg.norm(b)) or 1.0
    return float(np.dot(a, b) / denom)


def select_contexts(
    question: str, query_vec: np.ndarray, chunks: list[str], chunk_vecs: list[np.ndarray], k: int = 4
) -> list[str]:
    """Hybrid ranking: embedding score + keyword overlap."""
    q_tokens = _tokens(question)
    scored = []
    for i, chunk in enumerate(chunks):
        c_tokens = _tokens(chunk)
        overlap = len(q_tokens & c_tokens) / (len(q_tokens) or 1)
        sim = _cosine(query_vec, chunk_vecs[i])
        score = (0.8 * sim) + (0.2 * overlap)
        scored.append((score, chunk))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [chunk for _, chunk in scored[:k]]
