from pydantic import BaseModel, Field


class LeadInput(BaseModel):
    lead_name: str = Field(..., min_length=1)
    lead_role: str
    company_name: str
    company_industry: str
    company_size: str
    lead_source: str
    lead_notes: str


class LeadOutput(BaseModel):
    priority: str
    score: int
    why: str
    next_action: str
    crm_summary: str
