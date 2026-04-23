from knowledge_agent.chunking import chunk_documents
from knowledge_agent.embeddings import embed_query, embed_texts
from knowledge_agent.ingest import collect_documents
from knowledge_agent.reasoning import ask_llm
from knowledge_agent.retrieval import select_contexts


def answer_question(
    question: str,
    api_key: str,
    pasted_notes: str,
    uploaded_files: list,
) -> str:
    """Run full RAG: ingest -> chunk -> retrieve -> reason."""
    docs = collect_documents(pasted_notes, uploaded_files)
    if not docs:
        return "Please add notes or upload at least one file."

    chunks = chunk_documents(docs)
    if not chunks:
        return "Could not extract useful text from your documents."

    chunk_vecs = embed_texts(api_key, chunks)
    query_vec = embed_query(api_key, question)
    contexts = select_contexts(question, query_vec, chunks, chunk_vecs, k=4)
    return ask_llm(api_key, question, contexts)
