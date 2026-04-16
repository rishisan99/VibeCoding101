from openai import OpenAI


def run_prompt(api_key, prompt, model="gpt-4.1-mini"):
    """Run one OpenAI prompt and return (text, error)."""
    cleaned_key = (api_key or "").strip()
    if not cleaned_key:
        return None, "Missing OpenAI API key."

    cleaned_prompt = (prompt or "").strip()
    if not cleaned_prompt:
        return None, "Prompt is empty."

    try:
        client = OpenAI(api_key=cleaned_key)
        response = client.responses.create(
            model=model,
            input=cleaned_prompt,
            temperature=0,
        )
        output_text = (getattr(response, "output_text", "") or "").strip()
        if not output_text:
            return None, "Model returned an empty response."
        return output_text, None
    except Exception as exc:
        return None, f"OpenAI call failed: {exc}"
