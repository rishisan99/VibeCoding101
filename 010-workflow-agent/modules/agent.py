from modules.llm import ask_text

PROMPT = """Reply in this exact format:
STEPS:\n1. ...\nRESULTS:\n1. ...\nSUMMARY:\n...
Rules:
- Make 3 to 5 short steps.
- Each step should sound like a real work item.
- Make one short result line for each step.
- Results should sound like completed work with details.
- Keep the summary to 2 sentences max.
- Mention key issues, owners, deadlines, or next actions when present.
- Do not repeat the same wording across sections.
Workflow:
{workflow_text}"""


def _read_lines(block):
    return [line.strip(" -1234567890.") for line in block.splitlines() if line.strip(" -1234567890.")]


def _read_section(text, name, next_name):
    start = text.find(name)
    end = text.find(next_name) if next_name else len(text)
    return "" if start == -1 else text[start + len(name) : end].strip()


def run_agent(api_key, workflow_text):
    # Ask for a simple section-based response we can parse safely.
    text = ask_text(
        api_key,
        "You are a helpful workflow agent that turns messy requests into clear actions.",
        PROMPT.format(workflow_text=workflow_text),
    )
    steps = _read_lines(_read_section(text, "STEPS:", "RESULTS:"))
    results = _read_lines(_read_section(text, "RESULTS:", "SUMMARY:"))
    summary = _read_section(text, "SUMMARY:", "")
    if not steps or not results or not summary:
        raise ValueError(f"Unexpected model response:\n{text}")
    return {"steps": steps, "results": results, "summary": summary}
