from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph

from feedback_intelligence_agent.core.nodes import cluster_node
from feedback_intelligence_agent.core.nodes import ingest_node
from feedback_intelligence_agent.core.nodes import summarize_node


def build_graph():
    graph = StateGraph(dict)
    graph.add_node("ingest", ingest_node)
    graph.add_node("cluster", cluster_node)
    graph.add_node("summarize", summarize_node)
    graph.add_edge(START, "ingest")
    graph.add_edge("ingest", "cluster")
    graph.add_edge("cluster", "summarize")
    graph.add_edge("summarize", END)
    return graph.compile()
