from typing import TypedDict

from langgraph.graph import END, StateGraph

from app.llm import analyze_lead


class LeadState(TypedDict):
    lead: dict
    api_key: str
    result: dict


def run_analysis(state: LeadState) -> LeadState:
    state["result"] = analyze_lead(state["lead"], state["api_key"])
    return state


def build_graph():
    graph = StateGraph(LeadState)
    graph.add_node("analyze", run_analysis)
    graph.set_entry_point("analyze")
    graph.add_edge("analyze", END)
    return graph.compile()
