import chromadb
from langchain_openai import OpenAIEmbeddings

from config import CHROMA_DIR, EMBED_MODEL

RISK_QUERIES = ["risky legal or business language", "one sided obligations", "broad liability or termination issues"]
MISSING_QUERIES = ["important clauses that look missing", "weak protections or unclear duties", "missing renewal payment or dispute terms"]
COMPARE_TOPICS = ["termination", "payment", "liability", "confidentiality", "indemnity"]


def build_contexts(name: str, api_key: str, docs: list[str]) -> dict[str, str]:
    store = chromadb.PersistentClient(path=CHROMA_DIR).get_collection(name=name)
    embedder = OpenAIEmbeddings(model=EMBED_MODEL, api_key=api_key)
    return {"risk": join_queries(store, embedder, RISK_QUERIES), "missing": join_queries(store, embedder, MISSING_QUERIES), "compare": join_topics(store, embedder, docs)}


def join_queries(store, embedder, queries: list[str], limit: int = 3) -> str:
    blocks = []
    for query in queries:
        result = store.query(query_embeddings=[embedder.embed_query(query)], n_results=limit)
        blocks += format_blocks(query, result["documents"][0], result["metadatas"][0])
    return "\n\n".join(blocks)


def join_topics(store, embedder, docs: list[str]) -> str:
    blocks = []
    for topic in COMPARE_TOPICS:
        for doc in docs:
            result = store.query(query_embeddings=[embedder.embed_query(topic)], n_results=1, where={"contract": doc})
            blocks += format_blocks(topic, result["documents"][0], result["metadatas"][0])
    return "\n\n".join(blocks)


def format_blocks(label: str, texts: list[str], meta: list[dict]) -> list[str]:
    return [f"Focus: {label}\nContract: {item['contract']}\nText: {text}" for text, item in zip(texts, meta, strict=False)]
