import json

from openai import OpenAI

from finance_coach_agent.services.fallbacks import fallback_advice


def ask_llm(api_key: str, prompt: str, payload: dict) -> dict:
    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"{prompt}\n\nDATA:\n{json.dumps(payload)}",
        )
        return json.loads(response.output_text.strip())
    except Exception:
        return fallback_advice("The model response failed. Please try again.")
