import pandas as pd


def clean_positions(positions_json):
    df = pd.DataFrame(positions_json)

    useful_cols = [
        "driver_number",
        "date",
        "position",
    ]

    df = df[useful_cols].dropna()

    df["position"] = pd.to_numeric(df["position"])
    df["date"] = pd.to_datetime(df["date"])

    # =========================
    # # CREATE DERIVED LAP INDEX (based on time order)
    # =========================
    df = df.sort_values(["driver_number", "date"])

    df["lap_number"] = df.groupby("driver_number").cumcount() + 1

    return df
