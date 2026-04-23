import os
from pathlib import Path

from knowledge_agent.chunking import chunk_documents
from knowledge_agent.pipeline import answer_question


def main() -> None:
    notes = Path("sample_data/notes.md").read_text(encoding="utf-8")
    chunks = chunk_documents([notes])
    print(f"Loaded sample notes. Chunks: {len(chunks)}")

    key = os.getenv("OPENAI_API_KEY", "").strip()
    if not key:
        print("Set OPENAI_API_KEY to run full answer demo.")
        return

    q = "What does this project support and why does chunking matter?"
    ans = answer_question(q, key, notes, [])
    print("\nQuestion:", q)
    print("\nAnswer:\n", ans)


if __name__ == "__main__":
    main()
