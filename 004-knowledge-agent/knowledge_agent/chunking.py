def chunk_text(text: str, size: int = 800, overlap: int = 120) -> list[str]:
    """Chunk text by paragraphs with soft overlap."""
    blocks = [b.strip() for b in text.split("\n\n") if b.strip()]
    chunks, current = [], ""

    for block in blocks:
        candidate = f"{current}\n\n{block}".strip() if current else block
        if len(candidate) <= size:
            current = candidate
            continue
        if current:
            chunks.append(current)
        tail = current[-overlap:] if overlap and current else ""
        current = f"{tail}\n\n{block}".strip()
        if len(current) > size:
            chunks.append(current[:size])
            current = current[size - overlap :]

    if current:
        chunks.append(current)
    return [c for c in chunks if c.strip()]


def chunk_documents(docs: list[str]) -> list[str]:
    """Chunk all docs and keep only non-empty chunks."""
    out = []
    for doc in docs:
        out.extend(chunk_text(doc))
    return out
