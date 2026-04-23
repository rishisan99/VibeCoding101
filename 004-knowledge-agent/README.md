# Knowledge Agent

Simple RAG project for querying personal notes and PDFs.

## Run app

```bash
uv run streamlit run app.py
```

## Quick demo

```bash
uv run python demo.py
```

For full answer generation, set API key first:

```bash
export OPENAI_API_KEY="your_key_here"
uv run python demo.py
```

## How to use app

1. Paste your OpenAI API key in the sidebar (frontend).
2. Paste notes and/or upload `.txt`, `.md`, `.pdf` files.
3. Ask a question.
