import requests

from config import API_URL


def api_ready() -> bool:
    try:
        return requests.get(f"{API_URL}/health", timeout=3).ok
    except requests.RequestException:
        return False


def send_analysis(api_key: str, files) -> dict:
    payload = [("files", (file.name, file.getvalue(), file.type)) for file in files]
    response = requests.post(f"{API_URL}/analyze", data={"api_key": api_key}, files=payload, timeout=180)
    data = response.json() if response.content else {}
    if response.ok:
        return data
    raise ValueError(data.get("detail", "Backend request failed."))
