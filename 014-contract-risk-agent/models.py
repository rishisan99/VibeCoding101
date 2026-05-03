from pydantic import BaseModel, Field


class ClauseItem(BaseModel):
    clause: str
    reason: str
    contract: str


class InconsistencyItem(BaseModel):
    point: str
    contracts: list[str] = Field(default_factory=list)
    reason: str


class RiskReview(BaseModel):
    risky_clauses: list[ClauseItem] = Field(default_factory=list)


class MissingReview(BaseModel):
    missing_clauses: list[ClauseItem] = Field(default_factory=list)


class CompareReview(BaseModel):
    inconsistencies: list[InconsistencyItem] = Field(default_factory=list)
    cross_document_reasoning: list[str] = Field(default_factory=list)


class SummaryReview(BaseModel):
    final_summary: str


class AnalysisResult(BaseModel):
    risky_clauses: list[ClauseItem] = Field(default_factory=list)
    missing_clauses: list[ClauseItem] = Field(default_factory=list)
    inconsistencies: list[InconsistencyItem] = Field(default_factory=list)
    cross_document_reasoning: list[str] = Field(default_factory=list)
    final_summary: str
