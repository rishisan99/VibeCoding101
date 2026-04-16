from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_pages(
    pages: list[dict],
    chunk_size: int = 800,
    chunk_overlap: int = 120,
) -> list[dict]:
    """Split page text into chunks and keep simple metadata."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    all_chunks = []

    for page in pages:
        text_chunks = splitter.split_text(page["text"])
        for index, text in enumerate(text_chunks, start=1):
            all_chunks.append(
                {
                    "page": page["page"],
                    "chunk_id": f"p{page['page']}_c{index}",
                    "text": text.strip(),
                }
            )

    return all_chunks
