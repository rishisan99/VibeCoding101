def as_list(value: object, fallback: str) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value] or [fallback]
    if isinstance(value, str):
        return [value]
    return [fallback]


def as_text(value: object, fallback: str) -> str:
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) or fallback
    if isinstance(value, str):
        return value
    return fallback
