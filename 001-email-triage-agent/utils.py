"""Small helpers for JSON safety and fallback output."""

import json

from schema import empty_result


def parse_json(text: str) -> dict | None:
    """Parse JSON safely and return None on failure."""
    try:
        data = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None
    return data if isinstance(data, dict) else None


def error_result(message: str) -> dict:
    """Return schema-safe JSON with an error message."""
    data = empty_result()
    data["summary"] = "Could not analyze this email."
    data["error"] = message
    return data
