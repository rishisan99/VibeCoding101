def validate_files(files: list[dict]) -> None:
    if len(files) < 2:
        raise ValueError("Upload at least 2 contracts for comparison.")
    if any(not file["name"] for file in files):
        raise ValueError("Each uploaded file needs a name.")


def filter_docs(docs: list[dict]) -> list[dict]:
    clean = [doc for doc in docs if doc["text"].strip()]
    if len(clean) < 2:
        raise ValueError("Need readable text from at least 2 contracts.")
    return clean


def validate_chunks(chunks: list[dict]) -> None:
    if not chunks:
        raise ValueError("Could not build text chunks from the uploaded contracts.")
