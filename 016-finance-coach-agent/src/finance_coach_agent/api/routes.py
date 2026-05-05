from fastapi import APIRouter, HTTPException

from finance_coach_agent.graph.builder import build_graph
from finance_coach_agent.models.schemas import AdviceRequest
from finance_coach_agent.services.csv_parser import parse_csv_text
from finance_coach_agent.services.validator import validate_request, validate_rows

router = APIRouter()
graph = build_graph()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/plan")
def plan(request: AdviceRequest) -> dict:
    state = request.model_dump()
    request_errors = validate_request(state["goals"], state["csv_text"], state["expenses"])
    if request_errors:
        raise HTTPException(status_code=400, detail=request_errors)
    if state["csv_text"] and not state["expenses"]:
        state["expenses"] = parse_csv_text(state["csv_text"])
    row_errors = validate_rows(state["expenses"])
    if row_errors:
        raise HTTPException(status_code=400, detail=row_errors)
    return graph.invoke(state)
