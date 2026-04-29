from io import BytesIO

from pypdf import PdfReader


def parse_resume_text(filename: str | None, content: bytes) -> str:
    name = (filename or "").lower()
    if name.endswith(".pdf"):
        pages = PdfReader(BytesIO(content)).pages
        text = "\n".join(page.extract_text() or "" for page in pages)
        return text.strip()
    return content.decode("utf-8", errors="ignore").strip()
