SYSTEM_PROMPT = """
You are a sales lead qualification assistant.
Think like a sales manager.
Use business judgment, not rigid rules.
Return only valid JSON.
""".strip()


def build_prompt(data: dict) -> str:
    return f"""
Review this lead and classify it as hot, warm, or cold.

Weigh:
- buying intent
- company fit
- decision-maker seniority
- urgency
- use-case value

Lead data:
{data}

Return JSON with:
priority, score, why, next_action, crm_summary
""".strip()
