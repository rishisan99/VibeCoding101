# Feedback Intelligence Agent

Simple project for large-volume feedback analysis.

## Stack

- FastAPI for backend
- Streamlit for simple UI
- LangGraph for flow control
- Chroma for local vector storage
- OpenAI for reasoning tasks

## V1 Flow

1. Paste reviews or comments in the UI.
2. Split raw text into feedback items.
3. Store items for embedding search and clustering.
4. Group similar feedback into themes.
5. Summarize clusters into useful outputs.

## Local Run

1. Start API: `uv run uvicorn feedback_intelligence_agent.api.main:app --reload`
2. Start UI: `uv run streamlit run app.py`
3. Paste feedback and click `Analyze`
4. Use `Load Last Dataset` to reuse the latest pasted batch

## Outputs

- themes
- sentiment
- urgent issues
- feature requests
