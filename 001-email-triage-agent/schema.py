"""Schema for email triage output."""

ALLOWED_PRIORITIES = {"urgent", "action", "fyi"}

REQUIRED_KEYS = ["priority", "summary", "action_items", "reply_draft"]


def empty_result() -> dict:
    """Return a safe default response that matches our schema."""
    return {
        "priority": "fyi",
        "summary": "",
        "action_items": [],
        "reply_draft": "",
    }


def is_valid_result(data: dict) -> bool:
    """Basic schema check for model output."""
    if not isinstance(data, dict):
        return False
    if any(key not in data for key in REQUIRED_KEYS):
        return False
    if data["priority"] not in ALLOWED_PRIORITIES:
        return False
    if not isinstance(data["summary"], str):
        return False
    if not isinstance(data["action_items"], list):
        return False
    if not all(isinstance(item, str) for item in data["action_items"]):
        return False
    return isinstance(data["reply_draft"], str)
