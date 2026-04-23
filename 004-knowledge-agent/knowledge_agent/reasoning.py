from openai import OpenAI


def build_prompt(question: str, contexts: list[str]) -> str:
    """Create a short QA prompt with retrieved context."""
    joined = "\n\n".join(contexts)
    return (
        "Answer using only the context below. If not found, say you don't know.\n\n"
        f"Context:\n{joined}\n\n"
        f"Question: {question}\nAnswer:"
    )


def ask_llm(api_key: str, question: str, contexts: list[str]) -> str:
    """Call a small chat model for final answer."""
    client = OpenAI(api_key=api_key)
    prompt = build_prompt(question, contexts)
    res = client.responses.create(model="gpt-4.1-mini", input=prompt)
    return res.output_text.strip()
