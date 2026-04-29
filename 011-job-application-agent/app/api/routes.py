from fastapi import APIRouter, File, Form, UploadFile

from app.api.helpers import read_resume_text
from app.api.models import GenerateBody
from app.core.analyzer import analyze_inputs

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/analyze")
async def analyze(
    api_key: str = Form(""),
    job_description: str = Form(""),
    resume_file: UploadFile | None = File(default=None),
) -> dict[str, object]:
    resume_text = await read_resume_text(resume_file)
    return analyze_inputs(api_key, job_description, resume_text)


@router.post("/parse")
async def parse(resume_file: UploadFile | None = File(default=None)) -> dict[str, object]:
    resume_text = await read_resume_text(resume_file)
    return {"resume_text": resume_text, "chars": len(resume_text)}


@router.post("/generate")
def generate(data: GenerateBody) -> dict[str, object]:
    return analyze_inputs(data.api_key, data.job_description, data.resume_text)
