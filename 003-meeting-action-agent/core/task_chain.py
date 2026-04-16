from core.openai_client import run_prompt
from prompts.extract_actions import build_extract_actions_prompt
from prompts.structure_tasks import build_structure_tasks_prompt
from utils.task_parser import parse_tasks


def run_task_chain(api_key, notes, model="gpt-4.1-mini"):
    """Run prompt chain: notes -> raw actions -> structured tasks."""
    prompt_one = build_extract_actions_prompt(notes)
    raw_actions, error = run_prompt(api_key=api_key, prompt=prompt_one, model=model)
    if error:
        return {"tasks": [], "raw_actions": "", "structured_text": "", "error": error}

    prompt_two = build_structure_tasks_prompt(raw_actions)
    structured_text, error = run_prompt(api_key=api_key, prompt=prompt_two, model=model)
    if error:
        return {
            "tasks": [],
            "raw_actions": raw_actions,
            "structured_text": "",
            "error": error,
        }

    tasks = parse_tasks(structured_text)
    return {
        "tasks": tasks,
        "raw_actions": raw_actions,
        "structured_text": structured_text,
        "error": None,
    }
