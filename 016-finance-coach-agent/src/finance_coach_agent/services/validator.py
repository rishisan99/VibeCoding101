def validate_rows(rows: list[dict]) -> list[str]:
    errors = []
    if not rows:
        errors.append("No expense rows found in the CSV.")
    for index, row in enumerate(rows, start=1):
        if not row["category"]:
            errors.append(f"Row {index}: category is missing.")
        if row["amount"] < 0:
            errors.append(f"Row {index}: amount must be 0 or more.")
    return errors


def validate_request(goals: dict, csv_text: str, expenses: list[dict]) -> list[str]:
    errors = []
    if not csv_text.strip() and not expenses:
        errors.append("Paste a CSV or send expense rows.")
    if not any(goals.values()):
        errors.append("Add at least one goal before asking for advice.")
    return errors
