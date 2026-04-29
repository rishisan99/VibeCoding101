# Job Application Agent

Simple v1 app for resume and JD analysis.

## Run

```bash
uv run uvicorn app.main:app --reload
uv run streamlit run app/ui/streamlit_app.py
```

## V1 Scope

- one resume upload
- one job description paste box
- one analysis result
- no auth
- no saved history
- no database

## What It Returns

- fit score
- resume improvements
- tailored cover letter
- likely interview topics
