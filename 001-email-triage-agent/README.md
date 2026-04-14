# Email Triage Agent

Simple Streamlit app to triage emails with OpenAI.

## What It Returns

- `priority` (`urgent`, `action`, `fyi`)
- `summary`
- `action_items` (list of strings)
- `reply_draft`

## Run

```bash
uv sync
uv run streamlit run app.py
```

## Use

1. Paste OpenAI API key in sidebar.
2. Paste email text in input box.
3. Click **Analyze Email**.
4. Read JSON output.
