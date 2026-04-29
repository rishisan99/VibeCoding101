from typing import TypedDict


class AppState(TypedDict):
    api_key: str
    job_description: str
    resume_text: str
    context: list[str]
    result: dict[str, object]
