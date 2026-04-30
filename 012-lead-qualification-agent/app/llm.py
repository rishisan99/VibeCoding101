import json

from openai import OpenAI

from app.prompts import SYSTEM_PROMPT, build_prompt


def analyze_lead(data: dict, api_key: str) -> dict:
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(data)},
        ],
    )
    text = response.output_text.strip().replace("```json", "").replace("```", "")
    result = json.loads(text)
    result["score"] = int(result["score"])
    return result
