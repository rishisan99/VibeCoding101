from langgraph.graph import END, START, StateGraph

from finance_coach_agent.graph.nodes import apply_constraints, advise, summarize
from finance_coach_agent.graph.state import GraphState


def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("summarize", summarize)
    graph.add_node("advise", advise)
    graph.add_node("apply_constraints", apply_constraints)
    graph.add_edge(START, "summarize")
    graph.add_edge("summarize", "advise")
    graph.add_edge("advise", "apply_constraints")
    graph.add_edge("apply_constraints", END)
    return graph.compile()
