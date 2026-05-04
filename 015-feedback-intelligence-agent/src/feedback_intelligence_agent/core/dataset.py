from pathlib import Path

DATASET_FILE = Path("data/latest_feedback.txt")


def load_latest_feedback() -> str:
    if not DATASET_FILE.exists():
        return ""
    return DATASET_FILE.read_text()


def save_latest_feedback(text: str) -> None:
    # Keep the last pasted dataset so local testing is faster.
    DATASET_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATASET_FILE.write_text(text)
