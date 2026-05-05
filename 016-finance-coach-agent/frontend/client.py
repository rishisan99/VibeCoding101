import httpx


API_URL = "http://127.0.0.1:8000/plan"


def request_plan(api_key: str, csv_text: str, goals: dict) -> dict:
    payload = {"api_key": api_key, "csv_text": csv_text, "goals": goals, "expenses": []}
    response = httpx.post(API_URL, json=payload, timeout=60)
    response.raise_for_status()
    return response.json()
