def fallback_result(message: str) -> dict[str, object]:
    return {
        "fit_score": "Need API key",
        "resume_improvements": [message],
        "cover_letter": "Add your OpenAI API key to generate a tailored letter.",
        "interview_topics": ["Add your API key to generate interview topics."],
    }
