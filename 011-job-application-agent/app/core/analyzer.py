from app.core.graph import app_graph


def analyze_inputs(
    api_key: str,
    job_description: str,
    resume_text: str,
) -> dict[str, object]:
    state = app_graph.invoke(
        {
            "api_key": api_key,
            "job_description": job_description,
            "resume_text": resume_text,
            "context": [],
            "result": {},
        }
    )
    result = state["result"]
    result["meta"] = {
        "has_api_key": bool(api_key.strip()),
        "has_resume": bool(resume_text.strip()),
        "has_jd": bool(job_description.strip()),
        "resume_chars": len(resume_text),
        "context_chunks": len(state["context"]),
    }
    result["retrieved_context"] = state["context"]
    return result
