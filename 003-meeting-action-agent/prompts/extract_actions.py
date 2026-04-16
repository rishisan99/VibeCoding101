def build_extract_actions_prompt(notes):
    """Prompt 1: pull raw action items from meeting notes."""
    clean_notes = (notes or "").strip()

    return f"""
You are helping with meeting follow-up.

Goal:
Extract raw action items from the notes below.

Rules:
- Return only action items.
- Keep each item short.
- One item per line.
- Keep owner names if present (example: "Alice: finalize copy by Friday").
- Do not remove name prefixes like "Alice:" or "Bob:".
- If no action exists, return exactly: NO_ACTION_ITEMS

Meeting Notes:
{clean_notes}
""".strip()
