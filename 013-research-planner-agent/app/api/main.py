import uvicorn
from fastapi import FastAPI, HTTPException

from app.api.planner import build_plan
from app.models.schemas import ErrorResponse, PlannerResponse, TopicRequest

app = FastAPI(title="Research Planner API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/plan",
    response_model=PlannerResponse,
    responses={400: {"model": ErrorResponse}, 502: {"model": ErrorResponse}},
)
def create_plan(payload: TopicRequest) -> PlannerResponse:
    if not payload.topic.strip():
        raise HTTPException(status_code=400, detail="Topic is required.")
    if not payload.api_key.strip():
        raise HTTPException(status_code=400, detail="API key is required.")
    try:
        return build_plan(payload.topic, payload.api_key)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


def run() -> None:
    uvicorn.run("app.api.main:app", host="127.0.0.1", port=8000, reload=True)
