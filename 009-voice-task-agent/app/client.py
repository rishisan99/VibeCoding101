from openai import OpenAI


def get_client(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key)
