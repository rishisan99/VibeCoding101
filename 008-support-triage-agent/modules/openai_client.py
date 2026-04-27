import json

from openai import OpenAI


def analyze_ticket_with_ai(ticket, api_key):
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": get_system_prompt()},
            {"role": "user", "content": ticket},
        ],
    )

    content = response.choices[0].message.content
    return clean_result(json.loads(content))


def get_system_prompt():
    return """
You are a support triage assistant.
Return only JSON with these keys:
category, priority, team, response.

Use simple business language.
Priority must be High, Medium, or Low.
Response should be short and helpful.
"""


def clean_result(result):
    return {
        "category": result.get("category", "General Support"),
        "priority": result.get("priority", "Low"),
        "team": result.get("team", "Customer Support"),
        "response": result.get("response", "Thanks. We will review this soon."),
    }
