from feedback_intelligence_agent.core.dataset import save_latest_feedback
from feedback_intelligence_agent.core.graph import build_graph
from feedback_intelligence_agent.core.parser import parse_feedback
from feedback_intelligence_agent.core.results import empty_response
from feedback_intelligence_agent.core.results import pending_response
from feedback_intelligence_agent.core.schemas import AnalyzeResponse
from feedback_intelligence_agent.core.state import build_state


def analyze_feedback_text(
    text: str,
    flow: str,
    api_key: str | None,
) -> AnalyzeResponse:
    save_latest_feedback(text)
    items = parse_feedback(text)
    if not items:
        return empty_response(flow)
    if not api_key:
        return pending_response(flow, items, "Add OpenAI API key to run analysis")
    state = build_graph().invoke(build_state(text, flow, api_key))
    summary = state["summary"]
    return AnalyzeResponse(
        flow=flow,
        total_items=len(items),
        items=items,
        themes=summary["themes"],
        sentiment=summary["sentiment"],
        urgent_issues=summary["urgent_issues"],
        feature_requests=summary["feature_requests"],
    )
