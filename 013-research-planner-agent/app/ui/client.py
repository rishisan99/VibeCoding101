import requests

from app.core.config import REQUEST_TIMEOUT


def request_plan(api_url: str, topic: str, api_key: str) -> dict:
    try:
        response = requests.post(
            api_url,
            json={"topic": topic, "api_key": api_key},
            timeout=REQUEST_TIMEOUT,
        )
    except requests.RequestException as exc:
        raise RuntimeError("Backend is not reachable.") from exc
    if not response.ok:
        try:
            detail = response.json().get("detail", "Could not get plan from backend.")
        except ValueError:
            detail = "Could not get plan from backend."
        raise RuntimeError(detail)
    return response.json()
