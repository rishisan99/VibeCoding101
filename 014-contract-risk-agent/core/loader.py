from io import BytesIO

from docx import Document
from pypdf import PdfReader


def load_contracts(files: list[dict]) -> list[dict]:
    docs = []
    for file in files:
        text = read_text(file["name"], file["content"]).strip()
        docs.append({"name": file["name"], "text": text})
    return docs


def read_text(name: str, content: bytes) -> str:
    ext = name.rsplit(".", 1)[-1].lower()
    if ext == "txt":
        return content.decode("utf-8", errors="ignore")
    if ext == "pdf":
        reader = PdfReader(BytesIO(content))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if ext == "docx":
        doc = Document(BytesIO(content))
        return "\n".join(p.text for p in doc.paragraphs)
    raise ValueError(f"Unsupported file type: {name}")
