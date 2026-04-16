from .analyzer import analyze_retrieved_chunks
from .chunker import chunk_pages
from .output_formatter import normalize_insights
from .pdf_loader import extract_pdf_pages
from .vector_store import build_vector_store, retrieve_chunks


def _pack(pages, chunks, hits, insights=None, error=None) -> dict:
    return {
        "pages": pages,
        "chunks": chunks,
        "hits": hits,
        "insights": insights or {},
        "error": error,
    }


def run_rag_pipeline(uploaded_file, api_key: str) -> dict:
    """Run the full flow: extract, chunk, index, retrieve, summarize."""
    # Read plain text from the uploaded PDF.
    pages = extract_pdf_pages(uploaded_file)
    if not pages:
        return _pack([], [], [], error="No readable text found in this PDF.")
    chunks = chunk_pages(pages)
    if not chunks:
        return _pack(pages, [], [], error="Could not create text chunks from this PDF.")

    try:
        # Build vector index and fetch the most relevant chunks.
        collection = build_vector_store(chunks, api_key)
        hits = retrieve_chunks(collection, "key insights risks decisions", api_key, 6)
    except Exception:
        return _pack(
            pages, chunks, [], error="Failed while creating vectors or retrieving chunks."
        )

    try:
        # Ask the model to return structured JSON sections.
        insights = analyze_retrieved_chunks(hits, api_key)
        safe_insights = normalize_insights(insights)
    except Exception:
        return _pack(pages, chunks, hits, error="Failed while generating the final summary.")
    return _pack(pages, chunks, hits, insights=safe_insights)
