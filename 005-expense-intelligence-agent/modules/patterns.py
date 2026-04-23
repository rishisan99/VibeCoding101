import pandas as pd


def detect_patterns(df: pd.DataFrame) -> dict:
    """Find simple spending patterns for insights."""
    out = df.copy()
    out["date"] = pd.to_datetime(out["date"], errors="coerce")

    total = float(out["amount"].sum())
    by_category = out.groupby("category", as_index=False)["amount"].sum()
    by_category = by_category.sort_values("amount", ascending=False)

    by_month = out.dropna(subset=["date"]).copy()
    by_month["month"] = by_month["date"].dt.to_period("M").astype(str)
    by_month = by_month.groupby("month", as_index=False)["amount"].sum()

    avg_spend = float(out["amount"].mean())
    unusual = out[out["amount"] > (avg_spend * 1.8)][["date", "description", "amount"]]

    recurring = out.groupby("description", as_index=False).size()
    recurring = recurring[recurring["size"] > 1].sort_values("size", ascending=False)

    return {
        "total_spend": total,
        "by_category": by_category,
        "by_month": by_month,
        "unusual": unusual,
        "recurring": recurring,
    }
