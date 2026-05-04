FLOW_STEPS = [
    "Batch ingestion",
    "Embedding store",
    "Similarity clustering",
    "LLM summary",
    "Large-volume synthesis",
]


def flow_name() -> str:
    return "ingestion -> clustering -> summary"
