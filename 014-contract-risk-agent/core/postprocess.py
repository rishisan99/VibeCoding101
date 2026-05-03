from models import AnalysisResult


def clean_result(result: AnalysisResult) -> AnalysisResult:
    return AnalysisResult(
        risky_clauses=unique_items(result.risky_clauses, "clause"),
        missing_clauses=unique_items(result.missing_clauses, "clause"),
        inconsistencies=unique_items(result.inconsistencies, "point"),
        cross_document_reasoning=unique_lines(result.cross_document_reasoning),
        final_summary=result.final_summary.strip(),
    )


def unique_items(items: list, field: str) -> list:
    seen, keep = set(), []
    for item in items:
        contracts = tuple(getattr(item, "contracts", []))
        key = (getattr(item, field).lower(), contracts, getattr(item, "contract", None))
        if key not in seen and getattr(item, field).strip() and item.reason.strip():
            seen.add(key)
            keep.append(item)
    return keep


def unique_lines(lines: list[str]) -> list[str]:
    seen, keep = set(), []
    for line in lines:
        key = line.strip().lower()
        if key and key not in seen:
            seen.add(key)
            keep.append(line.strip())
    return keep
