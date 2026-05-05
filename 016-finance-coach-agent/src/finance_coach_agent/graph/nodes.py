from finance_coach_agent.graph.state import GraphState
from finance_coach_agent.services.advisor import get_advice, refine_advice


def summarize(state: GraphState) -> GraphState:
    total = sum(row["amount"] for row in state["expenses"])
    by_cat = {}
    for row in state["expenses"]:
        by_cat[row["category"]] = by_cat.get(row["category"], 0) + row["amount"]
    state["summary"] = {"total_spend": round(total, 2), "by_category": by_cat}
    return state


def advise(state: GraphState) -> GraphState:
    if not state["api_key"]:
        state["recommendations"] = {"message": "Add OpenAI API key to get advice."}
        return state
    payload = {"goals": state["goals"], "expenses": state["expenses"], "summary": state["summary"]}
    state["recommendations"] = get_advice(state["api_key"], payload)
    return state


def apply_constraints(state: GraphState) -> GraphState:
    if not state["api_key"] or "message" in state["recommendations"]:
        return state
    payload = {"goals": state["goals"], "summary": state["summary"], "advice": state["recommendations"]}
    state["recommendations"] = refine_advice(state["api_key"], payload)
    return state
