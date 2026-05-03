def build_chunks(docs: list[dict], size: int = 1200, overlap: int = 200) -> list[dict]:
    chunks = []
    step = size - overlap
    for doc in docs:
        text = clean_text(doc["text"])
        for start in range(0, len(text), step):
            part = text[start : start + size]
            if part.strip():
                chunks.append({"text": part, "contract": doc["name"]})
    return chunks


def clean_text(text: str) -> str:
    return " ".join(text.split())
