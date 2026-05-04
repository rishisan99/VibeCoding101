from feedback_intelligence_agent.core.cluster import cluster_feedback
from feedback_intelligence_agent.core.llm import embed_texts
from feedback_intelligence_agent.core.parser import parse_feedback
from feedback_intelligence_agent.core.store import save_feedback
from feedback_intelligence_agent.core.summarize import summarize_groups


def ingest_node(state: dict) -> dict:
    state["items"] = parse_feedback(state["text"])
    return state


def cluster_node(state: dict) -> dict:
    # We store vectors so the same batch can be inspected again in dev.
    vectors = embed_texts(state["api_key"], state["items"])
    docs, stored = save_feedback(state["items"], vectors)
    state["vectors"] = stored
    state["groups"] = cluster_feedback(docs, stored)
    return state


def summarize_node(state: dict) -> dict:
    state["summary"] = summarize_groups(state["api_key"], state["groups"])
    return state
