from app.core.llm import build_plan
from app.graph.state import PlannerState


def planner_node(state: PlannerState) -> dict:
    return {"plan": build_plan(state["topic"], state["api_key"])}
