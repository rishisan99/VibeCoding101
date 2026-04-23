from openai import OpenAI


def llm_recommendations(csv_text: str, api_key: str, model: str = "gpt-4o-mini") -> str:
    """Ask LLM for short practical savings advice."""
    client = OpenAI(api_key=api_key)
    prompt = "Give insights and 5 short savings recommendations from this expense CSV:\n" + csv_text
    res = client.responses.create(model=model, input=prompt)
    return res.output_text.strip()


def build_recommendations(df, api_key: str) -> dict:
    """Return LLM output only."""
    return {"llm": llm_recommendations(df.to_csv(index=False), api_key)}
