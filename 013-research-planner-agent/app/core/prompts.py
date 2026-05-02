SYSTEM_PROMPT = """
You are a research planning assistant.
Think like a human researcher.
Do not use rigid rule-based logic for planning.
Make the plan practical, clear, and topic-aware.
Keep the wording simple.
""".strip()

TASK_TEMPLATE = """
Topic: {topic}

Return 4 fields:
1. research_plan: short roadmap from scope to synthesis.
2. search_questions: 5 strong search questions.
3. source_strategy: what to search first and why.
4. output_template: a clean final notes template.
""".strip()


def get_user_prompt(topic: str) -> str:
    return TASK_TEMPLATE.format(topic=topic)


def get_system_prompt() -> str:
    return SYSTEM_PROMPT
