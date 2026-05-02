from typing import TypedDict

from app.models.schemas import PlannerResponse


class PlannerState(TypedDict):
    topic: str
    api_key: str
    plan: PlannerResponse | None
