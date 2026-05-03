from fastapi import FastAPI, File, Form, HTTPException, UploadFile

from services.analyze import analyze_contracts

app = FastAPI(title="Contract Risk Agent API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze")
async def analyze(
    api_key: str = Form(...),
    files: list[UploadFile] = File(...),
) -> dict:
    try:
        docs = []
        for file in files:
            docs.append({"name": file.filename, "content": await file.read()})
        return analyze_contracts(docs, api_key).model_dump()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Analysis failed. Check files and API key.") from exc
