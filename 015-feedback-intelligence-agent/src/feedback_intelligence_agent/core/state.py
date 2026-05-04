def build_state(text: str, flow: str, api_key: str) -> dict:
    return {
        "text": text,
        "flow": flow,
        "api_key": api_key,
        "items": [],
        "vectors": [],
        "groups": [],
        "summary": {},
    }
