from feedback_intelligence_agent.core.schemas import AnalyzeResponse


def empty_response(flow: str) -> AnalyzeResponse:
    return AnalyzeResponse(
        flow=flow,
        total_items=0,
        items=[],
        themes=["No feedback items found"],
        sentiment="No feedback items found",
        urgent_issues=["No feedback items found"],
        feature_requests=["No feedback items found"],
    )


def pending_response(flow: str, items: list[str], note: str) -> AnalyzeResponse:
    return AnalyzeResponse(
        flow=flow,
        total_items=len(items),
        items=items,
        themes=[note],
        sentiment=note,
        urgent_issues=[note],
        feature_requests=[note],
    )
