import json


def parse_json_text(text: str) -> dict:
    clean = text.replace("```json", "").replace("```", "").strip()
    if clean.startswith("{") and clean.endswith("}"):
        return json.loads(clean)
    start = clean.find("{")
    end = clean.rfind("}")
    if start >= 0 and end > start:
        return json.loads(clean[start : end + 1])
    raise ValueError("Model did not return valid JSON")
