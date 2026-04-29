import json
import os

from openai import OpenAI

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def generate_analysis(api_key: str, prompt: str) -> dict[str, object]:
    client = OpenAI(api_key=api_key)
    reply = client.chat.completions.create(
        model=MODEL,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": (
                    "You compare resumes to job descriptions. "
                    "Return JSON only with fit_score, resume_improvements, "
                    "cover_letter, and interview_topics."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )
    return json.loads(reply.choices[0].message.content or "{}")
