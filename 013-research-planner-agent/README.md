## Research Planner Agent

Simple project for turning a topic into:

- research plan
- search questions
- source strategy
- output template

Chosen stack for v1:

- FastAPI
- Streamlit
- LangGraph
- OpenAI
- uv

Project style:

- simple code
- modular files
- human-written comments
- no heavy rule-based planning

Run locally:

- `uv run run-api`
- `uv run streamlit run app/ui/main.py`

V1 keeps only the relevant tools:

- FastAPI
- Streamlit
- LangGraph
- OpenAI

Not used in v1:

- Chroma
- FAISS
- Whisper
- Playwright

App flow is in `docs/app_flow.md`.
