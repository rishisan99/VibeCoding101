import pandas as pd

REQUIRED_COLUMNS = ["date", "description", "amount", "balance_after"]


def validate_columns(df: pd.DataFrame) -> None:
    """Check required columns."""
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        cols = ", ".join(missing)
        raise ValueError(f"Missing required columns: {cols}")


def load_csv(file) -> pd.DataFrame:
    """Load and validate expense CSV."""
    df = pd.read_csv(file)
    validate_columns(df)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["balance_after"] = pd.to_numeric(df["balance_after"], errors="coerce")
    if df[["amount", "balance_after"]].isna().any().any():
        raise ValueError("amount and balance_after must be valid numbers")
    return df


def preview_data(df: pd.DataFrame, rows: int = 5) -> pd.DataFrame:
    """Return top rows for quick preview in UI."""
    return df.head(rows).copy()
