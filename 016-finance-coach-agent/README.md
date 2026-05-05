# Finance Coach Agent

Simple project base for:

- CSV expense input
- goal-aware planning
- advisory reasoning

## V1 stack

- FastAPI
- Streamlit
- LangGraph
- OpenAI

## Planned flow

1. Paste OpenAI API key in sidebar
2. Paste expense CSV
3. Add goals
4. Get recommendations

## Run later

```bash
uv run uvicorn finance_coach_agent.api.app:app --reload
uv run streamlit run frontend/app.py
```

## CSV shape

```csv
date,category,amount,note
2026-05-01,food,120,lunch
2026-05-02,transport,80,cab
```

You can also try the included sample file: [sample.csv](/Users/santhoshrishimarkonda/Desktop/Code/VibeCoding101/016-finance-coach-agent/sample.csv)
