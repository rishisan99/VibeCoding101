from langgraph.graph import END, START, StateGraph

from app.graph.nodes import planner_node
from app.graph.state import PlannerState

graph = StateGraph(PlannerState)
graph.add_node("planner", planner_node)
graph.add_edge(START, "planner")
graph.add_edge("planner", END)
planner_graph = graph.compile()


def run_planner(topic: str, api_key: str):
    state = {"topic": topic, "api_key": api_key, "plan": None}
    return planner_graph.invoke(state)["plan"]
