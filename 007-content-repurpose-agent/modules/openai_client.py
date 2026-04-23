from openai import OpenAI


def generate_text(api_key: str, prompt: str) -> str:
    # Small helper to call OpenAI once and return plain text.
    client = OpenAI(api_key=api_key)
    response = client.responses.create(model="gpt-4o-mini", input=prompt)
    return response.output_text.strip()
