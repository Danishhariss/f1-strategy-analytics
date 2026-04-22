import pandas as pd


def summarize_stints(stints_df):
    if stints_df.empty:
        return pd.DataFrame()

    summary = stints_df.groupby("driver_number").agg(
        total_stints=("stint_number", "count"),
        opening_compound=("compound", "first"),
        final_compound=("compound", "last"),
        longest_stint_laps=("stint_length", "max"),
        total_race_laps_from_stints=("stint_length", "sum"),
    )

    return summary


def get_selected_driver_stints(stints_df, driver_number):
    if stints_df.empty:
        return pd.DataFrame()

    driver_stints = stints_df[stints_df["driver_number"] == driver_number].copy()
    return driver_stints.sort_values("stint_number")


def build_strategy_story(driver_stints_df, driver_name):
    if driver_stints_df.empty:
        return f"No stint data available for {driver_name}."

    parts = []
    for _, row in driver_stints_df.iterrows():
        parts.append(
            f"Stint {int(row['stint_number'])}: {row['compound']} "
            f"(laps {int(row['lap_start'])}-{int(row['lap_end'])}, "
            f"{int(row['stint_length'])} laps)"
        )

    strategy_path = " → ".join(parts)
    return f"{driver_name}'s race strategy: {strategy_path}."
