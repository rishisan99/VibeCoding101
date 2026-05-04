from math import sqrt


def cluster_feedback(
    texts: list[str],
    vectors: list[list[float]],
    threshold: float = 0.72,
) -> list[list[str]]:
    clusters = []
    for text, vector in zip(texts, vectors):
        best = next((c for c in clusters if score(vector, c["center"]) >= threshold), None)
        if best:
            best["texts"].append(text)
            best["vectors"].append(vector)
            best["center"] = mean_vector(best["vectors"])
            continue
        clusters.append({"texts": [text], "vectors": [vector], "center": vector})
    return [cluster["texts"] for cluster in clusters]


def score(a: list[float], b: list[float]) -> float:
    top = sum(x * y for x, y in zip(a, b))
    bottom = sqrt(sum(x * x for x in a)) * sqrt(sum(y * y for y in b))
    return top / bottom if bottom else 0.0


def mean_vector(vectors: list[list[float]]) -> list[float]:
    size = len(vectors)
    return [sum(values) / size for values in zip(*vectors)]
