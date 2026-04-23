"""Utility helpers."""


def has_api_key(api_key: str) -> bool:
    """Check if the API key exists."""
    return bool(api_key and api_key.strip())
