# Meeting Action Agent

Convert meeting notes into a task list with:
- task
- owner
- deadline

The app uses prompt chaining:
1. Extract raw action items from notes
2. Structure items into `task | owner | deadline`

## Project Structure

- `app/main.py` - Streamlit app flow
- `app/ui.py` - Streamlit UI components
- `core/openai_client.py` - OpenAI API helper
- `core/task_chain.py` - Prompt chain service
- `prompts/` - Prompt builders
- `utils/task_parser.py` - Output parser

## Setup

Use your environment (Conda/venv) and install:

```bash
pip install streamlit openai python-dotenv
```

## Run

From project root:

```bash
streamlit run app/main.py
```

If needed:

```bash
python -m streamlit run app/main.py
```

## How to Use

1. Paste OpenAI API key in the sidebar.
2. Paste meeting notes (or use sample notes).
3. Click `Run`.
4. View tasks in the output table.

## Notes

- Owner is set to `UNKNOWN` only when not found in text.
- Deadline is set to `NO_DEADLINE` only when missing.
