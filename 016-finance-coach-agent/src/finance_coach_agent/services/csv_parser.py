import csv
from io import StringIO


def _clean_headers(row: dict) -> dict:
    return {str(key).strip().lower(): value for key, value in row.items()}


def parse_csv_text(text: str) -> list[dict]:
    reader = csv.DictReader(StringIO(text))
    rows = []
    for raw_row in reader:
        row = _clean_headers(raw_row)
        if not any(row.values()):
            continue
        rows.append(
            {
                "date": (row.get("date") or "").strip(),
                "category": (row.get("category") or "other").strip().lower(),
                "amount": float(row.get("amount") or 0),
                "note": (row.get("note") or "").strip(),
            }
        )
    return rows
