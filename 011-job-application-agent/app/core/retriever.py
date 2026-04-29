import uuid

import chromadb

from app.core.chunks import chunk_text

client = chromadb.EphemeralClient()


def fetch_resume_context(resume_text: str, job_description: str) -> list[str]:
    chunks = chunk_text(resume_text)
    if not chunks or not job_description.strip():
        return []
    name = f"resume-{uuid.uuid4().hex[:8]}"
    store = client.create_collection(name=name)
    store.add(ids=[f"c{i}" for i in range(len(chunks))], documents=chunks)
    found = store.query(query_texts=[job_description], n_results=min(4, len(chunks)))
    client.delete_collection(name=name)
    return found["documents"][0]
