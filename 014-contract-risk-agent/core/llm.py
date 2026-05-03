from langchain_openai import ChatOpenAI

from config import MODEL_NAME
from core.prompts import SYSTEM_PROMPT


def run_structured(schema, prompt: str, api_key: str):
    llm = ChatOpenAI(model=MODEL_NAME, api_key=api_key).with_structured_output(schema)
    return llm.invoke(f"{SYSTEM_PROMPT}\n\n{prompt}")
