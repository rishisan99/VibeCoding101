import json

from openai import OpenAI

from app.core.config import MODEL_NAME
from app.core.prompts import get_system_prompt, get_user_prompt
from app.models.schemas import PlannerResponse, planner_json_schema


def build_plan(topic: str, api_key: str) -> PlannerResponse:
    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=MODEL_NAME,
            instructions=get_system_prompt(),
            input=get_user_prompt(topic),
            text={"format": {
                "type": "json_schema",
                "name": "research_plan",
                "schema": planner_json_schema(),
                "strict": True,
            }},
        )
        return PlannerResponse(**json.loads(response.output_text))
    except Exception as exc:
        raise RuntimeError("OpenAI request failed. Check key and network.") from exc
