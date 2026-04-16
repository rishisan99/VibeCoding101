def parse_tasks(structured_text):
    """Parse 'task | owner | deadline' lines into a Python list."""
    clean_text = (structured_text or "").strip()
    if not clean_text or clean_text == "NO_ACTION_ITEMS":
        return []

    tasks = []
    for line in clean_text.splitlines():
        clean_line = line.strip()
        if not clean_line:
            continue

        parts = [part.strip() for part in clean_line.split("|")]
        if len(parts) != 3:
            continue

        task, owner, deadline = parts
        if not task:
            continue

        tasks.append(
            {"task": task, "owner": owner or "UNKNOWN", "deadline": deadline or "NO_DEADLINE"}
        )
    return tasks
