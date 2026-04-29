import json


def build_prompt(job_description: str, context: list[str]) -> str:
    body = {
        "job_description": job_description,
        "resume_context": context[:4],
        "fit_score_rule": "Return a number from 0 to 100.",
        "resume_improvements_rule": "Return 4 short bullets.",
        "cover_letter_rule": "Return one short tailored cover letter.",
        "interview_topics_rule": "Return 5 likely interview topics.",
    }
    return json.dumps(body, indent=2)
