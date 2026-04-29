def chunk_text(text: str, size: int = 700, overlap: int = 120) -> list[str]:
    clean = " ".join(text.split())
    if not clean:
        return []
    step = max(size - overlap, 1)
    return [clean[i : i + size] for i in range(0, len(clean), step)]
