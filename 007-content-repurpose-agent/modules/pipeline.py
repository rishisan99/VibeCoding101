from modules.openai_client import generate_text


def transform_text(api_key: str, source: str, input_fmt: str, output_fmt: str) -> str:
    # Keep prompts simple and practical.
    prompt = (
        f"Convert this {input_fmt} into a {output_fmt}.\n"
        "Keep meaning same, improve clarity, and keep natural tone.\n"
        "Output only final text.\n\n"
        f"Source:\n{source}"
    )
    return generate_text(api_key=api_key, prompt=prompt)
