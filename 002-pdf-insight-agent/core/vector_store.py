import chromadb
from openai import OpenAI


def embed_texts(texts: list[str], api_key: str) -> list[list[float]]:
    """Create embeddings for a list of texts."""
    client = OpenAI(api_key=api_key)
    res = client.embeddings.create(model="text-embedding-3-small", input=texts)
    return [item.embedding for item in res.data]


def build_vector_store(chunks: list[dict], api_key: str):
    """Embed chunks and store them in local Chroma DB."""
    # Keep vectors on disk so we can inspect them during development.
    client = chromadb.PersistentClient(path="data/vector_db")
    name = "pdf_chunks"
    try:
        client.delete_collection(name)
    except Exception:
        pass
    collection = client.create_collection(name=name)
    texts = [c["text"] for c in chunks]
    vectors = embed_texts(texts, api_key)
    ids = [c["chunk_id"] for c in chunks]
    metas = [{"page": c["page"]} for c in chunks]
    collection.upsert(ids=ids, documents=texts, metadatas=metas, embeddings=vectors)
    return collection


def retrieve_chunks(collection, query: str, api_key: str, top_k: int = 5) -> list[dict]:
    """Retrieve top chunks for a query."""
    q_vec = embed_texts([query], api_key)[0]
    res = collection.query(query_embeddings=[q_vec], n_results=top_k)
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    ids = res["ids"][0]
    return [{"chunk_id": i, "page": m["page"], "text": d} for i, m, d in zip(ids, metas, docs)]
