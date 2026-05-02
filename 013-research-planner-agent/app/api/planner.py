from app.graph.workflow import run_planner
from app.models.schemas import PlannerResponse


def build_plan(topic: str, api_key: str) -> PlannerResponse:
    return run_planner(topic.strip(), api_key.strip())
