def build_summary_prompt(groups: list[list[str]]) -> str:
    lines = []
    for index, group in enumerate(groups, start=1):
        joined = "\n".join(f"- {item}" for item in group)
        lines.append(f"Cluster {index}\n{joined}")
    body = "\n\n".join(lines)
    return (
        "Analyze the feedback clusters and return JSON with keys: "
        "themes, sentiment, urgent_issues, feature_requests. "
        "Each key must be simple English. Lists should be short.\n\n"
        f"{body}"
    )
