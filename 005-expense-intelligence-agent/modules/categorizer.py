import json
import pandas as pd
from openai import OpenAI

ALLOWED = ("Food", "Shopping", "Bills", "Subscriptions", "Learning", "Pet", "Other")


def _clean_category(text: str) -> str:
    mapping = {name.lower(): name for name in ALLOWED}
    raw = str(text).strip().lower()
    for key, value in mapping.items():
        if key in raw:
            return value
    return "Other"


def _parse_categories(raw: str, count: int) -> list[str]:
    try:
        data = json.loads(raw)
        if isinstance(data, list):
            cats = [_clean_category(item) for item in data]
            return (cats + ["Other"] * count)[:count]
    except Exception:
        pass
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    cats = [_clean_category(line) for line in lines]
    return (cats + ["Other"] * count)[:count]


def categorize_expenses(df: pd.DataFrame, api_key: str, model: str = "gpt-4o-mini") -> pd.DataFrame:
    """Add category using LLM only."""
    out = df.copy()
    client = OpenAI(api_key=api_key)
    rows = out["description"].fillna("").astype(str).tolist()
    prompt = (
        "Classify each expense description into one category: "
        "Food, Shopping, Bills, Subscriptions, Learning, Pet, Other.\n"
        "Return only a JSON array in the same order.\n"
        "Descriptions:\n- " + "\n- ".join(rows)
    )
    res = client.responses.create(model=model, input=prompt)
    cats = _parse_categories(res.output_text, len(out))
    out["category"] = cats
    return out
