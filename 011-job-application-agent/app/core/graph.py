from langgraph.graph import END, START, StateGraph

from app.core.fallback import fallback_result
from app.core.llm import generate_analysis
from app.core.prompt import build_prompt
from app.core.retriever import fetch_resume_context
from app.core.state import AppState


def retrieve_node(state: AppState) -> AppState:
    # Keep retrieval small and focused before generation.
    if (
        state["api_key"].strip()
        and state["resume_text"].strip()
        and state["job_description"].strip()
    ):
        state["context"] = fetch_resume_context(state["resume_text"], state["job_description"])
    return state


def generate_node(state: AppState) -> AppState:
    if not state["api_key"].strip():
        state["result"] = fallback_result("Add your OpenAI API key in the sidebar.")
        return state
    try:
        prompt = build_prompt(state["job_description"], state["context"])
        state["result"] = generate_analysis(state["api_key"], prompt)
    except Exception:
        state["result"] = fallback_result("The model call failed. Check your key and try again.")
    return state


graph = StateGraph(AppState)
graph.add_node("retrieve", retrieve_node)
graph.add_node("generate", generate_node)
graph.add_edge(START, "retrieve")
graph.add_edge("retrieve", "generate")
graph.add_edge("generate", END)
app_graph = graph.compile()
