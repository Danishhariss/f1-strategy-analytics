import pandas as pd


def clean_pit_stops(pit_json):
    if pit_json is None:
        return pd.DataFrame()

    # ⚠️ THIS IS YOUR MAIN FIX
    if isinstance(pit_json, dict):
        print("\nUnexpected pit stop response:")
        print(pit_json)
        return pd.DataFrame()

    if not isinstance(pit_json, list) or len(pit_json) == 0:
        return pd.DataFrame()

    df = pd.DataFrame(pit_json)

    useful_cols = ["driver_number", "date", "lap_number"]
    existing_cols = [col for col in useful_cols if col in df.columns]

    if not existing_cols:
        return pd.DataFrame()

    df = df[existing_cols].dropna()

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    if "lap_number" in df.columns:
        df["lap_number"] = pd.to_numeric(df["lap_number"])

    return df.sort_values(["driver_number", "date"])
