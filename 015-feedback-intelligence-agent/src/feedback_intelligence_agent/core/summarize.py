from feedback_intelligence_agent.core.llm import read_json
from feedback_intelligence_agent.core.normalize import as_list
from feedback_intelligence_agent.core.normalize import as_text
from feedback_intelligence_agent.core.prompts import build_summary_prompt


def summarize_groups(api_key: str, groups: list[list[str]]) -> dict:
    prompt = build_summary_prompt(groups)
    data = read_json(api_key, prompt)
    return {
        "themes": as_list(data.get("themes"), "Theme synthesis failed"),
        "sentiment": as_text(data.get("sentiment"), "Sentiment synthesis failed"),
        "urgent_issues": as_list(data.get("urgent_issues"), "Urgent issue synthesis failed"),
        "feature_requests": as_list(
            data.get("feature_requests"),
            "No clear feature requests found",
        ),
    }
