"""Simple OpenAI agent for email triage."""

from openai import OpenAI

from schema import is_valid_result
from utils import error_result, parse_json

SYSTEM_PROMPT = """
You are an email triage assistant.
Classify email priority as one of: urgent, action, fyi.
Return JSON with keys: priority, summary, action_items, reply_draft.
Keep summary short and clear.
Action items must be a list of strings.
Reply draft should be polite and practical.
""".strip()


def triage_email(api_key: str, email_text: str, model: str = "gpt-4.1-mini") -> dict:
    """Analyze one email and return structured JSON."""
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": email_text},
            ],
        )
    except Exception as exc:
        return error_result(f"API error: {exc}")
    text = response.choices[0].message.content or "{}"
    data = parse_json(text)
    if data is None:
        return error_result("Model returned invalid JSON.")
    if not is_valid_result(data):
        return error_result("Model JSON did not match schema.")
    return data
