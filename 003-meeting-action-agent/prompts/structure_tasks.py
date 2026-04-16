def build_structure_tasks_prompt(raw_actions):
    """Prompt 2: convert raw actions to task, owner, deadline."""
    clean_actions = (raw_actions or "").strip()

    return f"""
You are a task structuring assistant.

Goal:
Convert each raw action into this format:
task | owner | deadline

Rules:
- Keep one task per line.
- If line starts with "Name: ...", set owner = Name.
- If line starts with "Team: ...", set owner = Team.
- Use UNKNOWN when owner is missing.
- Use NO_DEADLINE when deadline is missing.
- Do not add extra text or headings.
- If input is NO_ACTION_ITEMS, return exactly: NO_ACTION_ITEMS

Raw Actions:
{clean_actions}
""".strip()
