import re


def parse_feedback(text: str) -> list[str]:
    items = []
    for line in text.splitlines():
        clean = re.sub(r"^\s*(?:[-*]|\d+[.)])\s*", "", line).strip()
        parts = split_line(clean)
        items.extend(parts)
    return items


def split_line(text: str) -> list[str]:
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [part.strip(" -") for part in parts if part.strip(" -")]
