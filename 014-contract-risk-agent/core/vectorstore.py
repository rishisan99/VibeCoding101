from pathlib import Path
from uuid import uuid4

import chromadb
from langchain_openai import OpenAIEmbeddings

from config import CHROMA_DIR, EMBED_MODEL


def build_collection(chunks: list[dict], api_key: str) -> str:
    Path(CHROMA_DIR).mkdir(parents=True, exist_ok=True)
    name = f"contracts-{uuid4().hex}"
    texts = [chunk["text"] for chunk in chunks]
    meta = [{"contract": chunk["contract"]} for chunk in chunks]
    ids = [f"chunk-{i}" for i in range(len(chunks))]
    store = chromadb.PersistentClient(path=CHROMA_DIR).create_collection(name=name)
    vectors = OpenAIEmbeddings(model=EMBED_MODEL, api_key=api_key).embed_documents(texts)
    store.add(ids=ids, documents=texts, metadatas=meta, embeddings=vectors)
    return name


def drop_collection(name: str) -> None:
    chromadb.PersistentClient(path=CHROMA_DIR).delete_collection(name)
