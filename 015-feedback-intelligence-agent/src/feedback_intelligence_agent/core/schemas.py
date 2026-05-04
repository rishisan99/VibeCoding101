from pydantic import BaseModel

from feedback_intelligence_agent.core.flow import flow_name


class AnalyzeRequest(BaseModel):
    feedback: str
    api_key: str | None = None
    flow_name: str = flow_name()


class AnalyzeResponse(BaseModel):
    flow: str
    total_items: int
    items: list[str]
    themes: list[str]
    sentiment: str
    urgent_issues: list[str]
    feature_requests: list[str]
