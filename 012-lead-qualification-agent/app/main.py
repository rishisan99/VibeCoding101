from fastapi import FastAPI, Header, HTTPException

from app.graph import build_graph
from app.schemas import LeadInput, LeadOutput

app = FastAPI(title="Lead Qualification Agent")
graph = build_graph()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=LeadOutput)
def analyze(data: LeadInput, x_api_key: str | None = Header(default=None)):
    if not x_api_key:
        raise HTTPException(status_code=400, detail="Missing x-api-key header")
    state = {"lead": data.model_dump(), "api_key": x_api_key, "result": {}}
    return graph.invoke(state)["result"]
