import os

import httpx

BASE_URL = os.getenv("API_URL", "http://127.0.0.1:8000")


def parse_resume(resume_file) -> dict[str, object]:
    files = {}
    if resume_file:
        file_type = resume_file.type or "application/octet-stream"
        files["resume_file"] = (resume_file.name, resume_file.getvalue(), file_type)
    response = httpx.post(f"{BASE_URL}/parse", files=files, timeout=60)
    response.raise_for_status()
    return response.json()


def post_analysis(api_key: str, job_description: str, resume_file) -> dict[str, object]:
    data = {"api_key": api_key, "job_description": job_description}
    files = {}
    if resume_file:
        file_type = resume_file.type or "application/octet-stream"
        files["resume_file"] = (resume_file.name, resume_file.getvalue(), file_type)
    response = httpx.post(f"{BASE_URL}/analyze", data=data, files=files, timeout=60)
    response.raise_for_status()
    return response.json()
