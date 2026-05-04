from fastapi import FastAPI
from fastapi import HTTPException

from feedback_intelligence_agent.core.analyze import analyze_feedback_text
from feedback_intelligence_agent.core.error_text import user_error_text
from feedback_intelligence_agent.core.schemas import AnalyzeRequest
from feedback_intelligence_agent.core.schemas import AnalyzeResponse

app = FastAPI(title="Feedback Intelligence API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_feedback(body: AnalyzeRequest) -> AnalyzeResponse:
    try:
        return analyze_feedback_text(body.feedback, body.flow_name, body.api_key)
    except Exception as error:
        raise HTTPException(status_code=500, detail=user_error_text(error))
