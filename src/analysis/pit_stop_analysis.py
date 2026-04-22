import pandas as pd


def summarize_pit_stops(pit_df):
    if pit_df.empty:
        return pd.DataFrame()

    summary = pit_df.groupby("driver_number").agg(
        total_pit_stops=("lap_number", "count"),
        first_pit_lap=("lap_number", "min"),
        last_pit_lap=("lap_number", "max"),
    )

    return summary
