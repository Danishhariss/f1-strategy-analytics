def position_change_summary(positions_df):
    summary = positions_df.groupby("driver_number")["position"].agg(
        start_position="first",
        end_position="last"
    )

    summary["positions_gained"] = (
        summary["start_position"] - summary["end_position"]
    )

    return summary.sort_values("positions_gained", ascending=False)
