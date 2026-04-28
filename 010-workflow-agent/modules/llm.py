from openai import OpenAI

MODEL = "gpt-4.1-mini"


def ask_text(api_key, instructions, prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt},
        ],
        max_tokens=400,
    )
    text = response.choices[0].message.content or ""
    text = text.strip()
    if not text:
        raise ValueError("Model returned an empty message.")
    return text
