from chromadb import Client
from chromadb.config import Settings


def build_store() -> Client:
    # Persist locally so we can reuse the same feedback set in dev.
    settings = Settings(is_persistent=True, persist_directory="data/chroma")
    return Client(settings)


def collection_name(vectors: list[list[float]]) -> str:
    size = len(vectors[0]) if vectors else 0
    return f"feedback_items_{size}d"


def save_feedback(
    items: list[str],
    vectors: list[list[float]],
) -> tuple[list[str], list[list[float]]]:
    ids = [f"feedback-{index}" for index, _ in enumerate(items, start=1)]
    docs = build_store().get_or_create_collection(collection_name(vectors))
    docs.upsert(ids=ids, documents=items, embeddings=vectors)
    data = docs.get(ids=ids, include=["documents", "embeddings"])
    return data["documents"], data["embeddings"]
