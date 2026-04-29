from pydantic import BaseModel


class GenerateBody(BaseModel):
    api_key: str = ""
    job_description: str = ""
    resume_text: str = ""
