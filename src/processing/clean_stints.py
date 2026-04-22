import pandas as pd


def clean_stints(stints_json):
    if stints_json is None:
        return pd.DataFrame()

    if isinstance(stints_json, dict):
        print("\nUnexpected stints response:")
        print(stints_json)
        return pd.DataFrame()

    if not isinstance(stints_json, list) or len(stints_json) == 0:
        return pd.DataFrame()

    df = pd.DataFrame(stints_json)

    useful_cols = [
        "driver_number",
        "stint_number",
        "compound",
        "lap_start",
        "lap_end",
        "tyre_age_at_start",
    ]

    existing_cols = [col for col in useful_cols if col in df.columns]
    df = df[existing_cols].copy()

    if "stint_number" in df.columns:
        df["stint_number"] = pd.to_numeric(df["stint_number"], errors="coerce")

    if "lap_start" in df.columns:
        df["lap_start"] = pd.to_numeric(df["lap_start"], errors="coerce")

    if "lap_end" in df.columns:
        df["lap_end"] = pd.to_numeric(df["lap_end"], errors="coerce")

    if "tyre_age_at_start" in df.columns:
        df["tyre_age_at_start"] = pd.to_numeric(df["tyre_age_at_start"], errors="coerce")

    df = df.dropna(subset=["driver_number", "stint_number", "compound", "lap_start", "lap_end"])

    df["stint_length"] = df["lap_end"] - df["lap_start"] + 1

    return df.sort_values(["driver_number", "stint_number"])
