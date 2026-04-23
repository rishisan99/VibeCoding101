"""Tool-calling agent flow."""

import json

from openai import OpenAI

from prompts import AGENT_SYSTEM_PROMPT, SUMMARY_USER_PROMPT
from tools import search_web

TOOLS = [{
    "type": "function",
    "name": "search_web",
    "description": "Search the web for trusted sources.",
    "parameters": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
        "additionalProperties": False,
    },
}]


def run_research(query: str, api_key: str) -> dict:
    """Run: model -> tool call -> model summary."""
    client, sources = OpenAI(api_key=api_key), []
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": AGENT_SYSTEM_PROMPT},
            {"role": "user", "content": f"Topic: {query}\n{SUMMARY_USER_PROMPT}"},
        ],
        tools=TOOLS,
    )

    while True:
        # If model asks for a tool, run it and send back the result.
        calls = [o for o in response.output if getattr(o, "type", "") == "function_call"]
        if not calls:
            break
        outputs = []
        for call in calls:
            args = json.loads(call.arguments or "{}")
            sources = search_web(query=args.get("query", query), api_key=api_key)
            outputs.append({"type": "function_call_output", "call_id": call.call_id, "output": json.dumps(sources)})
        response = client.responses.create(model="gpt-4.1-mini", previous_response_id=response.id, input=outputs)

    return {"summary": response.output_text, "sources": sources}
