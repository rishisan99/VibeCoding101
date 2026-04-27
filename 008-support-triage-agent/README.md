# Support Triage Agent

A simple Streamlit app for support ticket triage.

## Run

```bash
uv run streamlit run app.py
```

Open the local URL Streamlit prints in the terminal.

## Goal

- Classify support tickets
- Assign priority
- Suggest the right team
- Draft a helpful response

## How it works

- Paste a ticket
- Add an OpenAI API key in the sidebar if you want AI analysis
- Leave the key blank to use local keyword rules
