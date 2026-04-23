import numpy as np
from openai import OpenAI


def _to_array(vec: list[float]) -> np.ndarray:
    """Convert list vector to numpy array."""
    return np.array(vec, dtype=float)


def embed_texts(api_key: str, texts: list[str]) -> list[np.ndarray]:
    """Create embeddings for many text chunks."""
    client = OpenAI(api_key=api_key)
    res = client.embeddings.create(model="text-embedding-3-small", input=texts)
    return [_to_array(item.embedding) for item in res.data]


def embed_query(api_key: str, question: str) -> np.ndarray:
    """Create embedding for user question."""
    client = OpenAI(api_key=api_key)
    res = client.embeddings.create(model="text-embedding-3-small", input=question)
    return _to_array(res.data[0].embedding)
