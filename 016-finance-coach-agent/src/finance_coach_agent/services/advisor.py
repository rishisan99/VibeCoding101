from finance_coach_agent.core.prompts import ADVICE_PROMPT, CONSTRAINT_PROMPT
from finance_coach_agent.services.llm_client import ask_llm


def get_advice(api_key: str, payload: dict) -> dict:
    return ask_llm(api_key, ADVICE_PROMPT, payload)


def refine_advice(api_key: str, payload: dict) -> dict:
    return ask_llm(api_key, CONSTRAINT_PROMPT, payload)
