from openai import OpenAI

from feedback_intelligence_agent.core.json_utils import parse_json_text


def build_llm(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key)


def embed_texts(api_key: str, texts: list[str]) -> list[list[float]]:
    client = build_llm(api_key)
    result = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )
    return [item.embedding for item in result.data]


def read_json(api_key: str, prompt: str) -> dict:
    client = build_llm(api_key)
    result = client.responses.create(model="gpt-4.1-mini", input=prompt)
    return parse_json_text(result.output_text)
