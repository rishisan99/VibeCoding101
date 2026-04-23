"""Tool wrappers used by the agent."""

from openai import OpenAI


def search_web(query: str, api_key: str, limit: int = 5) -> list[dict]:
    """Search the web and return clean source links."""
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Find reliable sources for: {query}",
        tools=[{"type": "web_search_preview"}],
    )

    # Read citations from the response and keep only unique links.
    seen, items = set(), []
    for block in response.output:
        if getattr(block, "type", "") != "message":
            continue
        for content in getattr(block, "content", []):
            for ann in getattr(content, "annotations", []):
                url = getattr(ann, "url", "")
                if not url or url in seen:
                    continue
                seen.add(url)
                title = getattr(ann, "title", "") or url
                items.append({"title": title, "url": url})
    return items[:limit]
