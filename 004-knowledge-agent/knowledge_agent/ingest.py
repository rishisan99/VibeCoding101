from pypdf import PdfReader


def _read_pdf(uploaded_file) -> str:
    """Extract text from one uploaded PDF."""
    reader = PdfReader(uploaded_file)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages).strip()


def _read_note(uploaded_file) -> str:
    """Read text from uploaded txt or md file."""
    raw = uploaded_file.getvalue()
    return raw.decode("utf-8", errors="ignore").strip()


def collect_documents(pasted_notes: str, uploaded_files: list) -> list[str]:
    """Collect docs from pasted notes and uploaded files."""
    docs = [pasted_notes.strip()] if pasted_notes.strip() else []
    for file in uploaded_files or []:
        if file.name.lower().endswith(".pdf"):
            text = _read_pdf(file)
        else:
            text = _read_note(file)
        if text:
            docs.append(text)
    return docs
