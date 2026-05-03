## Contract Risk Agent

### Run

```bash
uv run uvicorn api:app --reload
uv run streamlit run app.py
```

### Test

```bash
uv run python -m unittest discover -s tests
```

### Current Scope

- Step 5: Streamlit UI
- Step 6: FastAPI API
- Step 7: file loading for pdf, docx, txt
- Step 8: Chroma vector store with OpenAI embeddings
- Step 9: LangGraph workflow for ingest, retrieve, review
- Step 10-13: compare, risk, missing, and final report stages
- Step 14-16: validation, polish, and smoke tests
