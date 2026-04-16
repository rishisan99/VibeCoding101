from io import BytesIO

from pypdf import PdfReader


def extract_pdf_pages(uploaded_file) -> list[dict]:
    """Extract plain text from each PDF page."""
    if uploaded_file is None:
        return []

    pdf_bytes = uploaded_file.getvalue()
    reader = PdfReader(BytesIO(pdf_bytes))
    pages = []

    for index, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if text:
            pages.append({"page": index, "text": text})

    return pages
