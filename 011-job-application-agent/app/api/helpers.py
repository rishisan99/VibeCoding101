from fastapi import UploadFile

from app.core.parser import parse_resume_text


async def read_resume_text(resume_file: UploadFile | None) -> str:
    if not resume_file:
        return ""
    return parse_resume_text(resume_file.filename, await resume_file.read())
