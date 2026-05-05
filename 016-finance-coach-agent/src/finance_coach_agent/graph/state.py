from typing import TypedDict


class GraphState(TypedDict):
    api_key: str
    goals: dict
    expenses: list[dict]
    summary: dict
    recommendations: dict
