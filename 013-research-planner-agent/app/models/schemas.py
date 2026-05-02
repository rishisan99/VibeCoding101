from pydantic import BaseModel, ConfigDict, Field


class TopicRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    topic: str = Field(min_length=1)
    api_key: str = Field(min_length=1)


class PlannerResponse(BaseModel):
    research_plan: str = Field(description="Main research roadmap.")
    search_questions: list[str] = Field(description="Questions to search.")
    source_strategy: str = Field(description="How to choose sources.")
    output_template: str = Field(description="Final notes template.")


class ErrorResponse(BaseModel):
    detail: str


def planner_json_schema() -> dict:
    return {
        "type": "object",
        "properties": {
            "research_plan": {"type": "string"},
            "search_questions": {"type": "array", "items": {"type": "string"}},
            "source_strategy": {"type": "string"},
            "output_template": {"type": "string"},
        },
        "required": [
            "research_plan",
            "search_questions",
            "source_strategy",
            "output_template",
        ],
        "additionalProperties": False,
    }
