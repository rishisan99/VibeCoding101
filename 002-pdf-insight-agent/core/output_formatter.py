def normalize_insights(data: dict) -> dict:
    """Normalize model output into safe list-based sections."""
    keys = ["key_insights", "risks", "decisions"]
    normalized = {}

    for key in keys:
        value = data.get(key, [])
        if isinstance(value, str):
            normalized[key] = [value.strip()] if value.strip() else []
        elif isinstance(value, list):
            normalized[key] = [str(item).strip() for item in value if str(item).strip()]
        else:
            normalized[key] = []

    raw = data.get("raw")
    if raw:
        normalized["raw"] = str(raw)
    return normalized
