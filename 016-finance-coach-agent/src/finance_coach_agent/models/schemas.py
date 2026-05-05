from pydantic import BaseModel, Field


class GoalInput(BaseModel):
    savings_target: float = Field(default=0, ge=0)
    spending_limit: float = Field(default=0, ge=0)
    focus_category: str = ""
    month: str = ""


class ExpenseRow(BaseModel):
    date: str
    category: str
    amount: float
    note: str = ""


class AdviceRequest(BaseModel):
    api_key: str = ""
    goals: GoalInput
    expenses: list[ExpenseRow] = Field(default_factory=list)
    csv_text: str = ""
