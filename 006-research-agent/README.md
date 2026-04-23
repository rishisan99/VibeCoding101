# Simple Research Agent

A small Streamlit app that:
- searches the web
- summarizes findings
- shows source links

## Setup (uv)
```bash
uv sync
```

## Run
```bash
uv run streamlit run app.py
```

## How to use
1. Open the app in browser.
2. Paste your OpenAI API key in the sidebar.
3. Enter a research topic and click `Research`.

## Project files
- `app.py` - Streamlit UI
- `agent.py` - tool-calling agent flow
- `tools.py` - web search tool wrapper
- `prompts.py` - short prompts
- `utils.py` - small helpers
