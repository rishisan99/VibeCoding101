# PDF Insight Agent

Simple RAG app to read a PDF and extract:
- key insights
- risks
- decisions

## What you learn
- Basic RAG pipeline
- PDF loading
- Chunking with overlap
- Embeddings + vector DB
- Retrieval + summarization

## Tech
- Streamlit UI
- `pypdf` PDF loader
- OpenAI embeddings + LLM
- Chroma local vector DB
- `uv` package manager

## Project flow
1. Upload PDF
2. Extract text by page
3. Chunk text
4. Create embeddings + store vectors
5. Retrieve top chunks
6. Summarize into structured output

## Run with uv
```bash
uv sync
uv run streamlit run app/main.py
```

## Notes
- Paste your OpenAI API key in the sidebar.
- Vector DB is stored in `data/vector_db`.
- If PDF text is not readable, the app shows a friendly error.
