import json

from openai import OpenAI


def _clean_json_text(text: str) -> str:
    """Remove markdown fences so json.loads can parse safely."""
    clean = text.strip()
    if clean.startswith("```"):
        clean = clean.split("\n", 1)[1] if "\n" in clean else clean
        clean = clean.rsplit("```", 1)[0]
    return clean.strip()


def analyze_retrieved_chunks(chunks: list[dict], api_key: str) -> dict:
    """Summarize retrieved chunks into key insights, risks, and decisions."""
    client = OpenAI(api_key=api_key)
    # Include chunk id and page so outputs can be traced back later.
    context = "\n\n".join(
        [f"[{c['chunk_id']}|p{c['page']}] {c['text']}" for c in chunks]
    )
    prompt = (
        "Use only the context and return strict JSON with keys: "
        "key_insights, risks, decisions. Each value must be a list of short bullets.\n\n"
        f"Context:\n{context}"
    )
    res = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=0,
    )
    text = _clean_json_text(res.output_text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"key_insights": [], "risks": [], "decisions": [], "raw": text}
