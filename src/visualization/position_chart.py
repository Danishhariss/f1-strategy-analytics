import matplotlib.pyplot as plt


def plot_position_trends(
    positions_df,
    driver_map,
    selected_drivers=None,
    stints_df=None,
    top_n=5,
):
    """
    Plot race position changes over time
    + overlay stint changes
    """

    if selected_drivers is not None:
        drivers_to_plot = selected_drivers
    else:
        summary = positions_df.groupby("driver_number")["position"].agg(
            start_position="first",
            end_position="last"
        )
        summary["positions_gained"] = summary["start_position"] - summary["end_position"]

        drivers_to_plot = (
            summary.sort_values("positions_gained", ascending=False)
            .head(top_n)
            .index
            .tolist()
        )

    filtered = positions_df[positions_df["driver_number"].isin(drivers_to_plot)]

    plt.figure(figsize=(12, 6))

    for driver_number in drivers_to_plot:
        driver_data = filtered[filtered["driver_number"] == driver_number].copy()
        driver_name = driver_map.get(driver_number, str(driver_number))

        driver_data["lap_index"] = driver_data["lap_number"]
        driver_data = driver_data.sort_values("lap_index")

        plt.plot(
            driver_data["lap_index"],
            driver_data["position"],
            label=driver_name,
            marker="o",
            markersize=3
        )

        # Add stint markers
        if stints_df is not None:
            driver_stints = stints_df[
                stints_df["driver_number"] == driver_number
            ].dropna(subset=["lap_start"]).sort_values("lap_start")


            print(f"\nStints for {driver_name}:")
            print(driver_stints[["stint_number", "compound", "lap_start", "lap_end", "stint_length"]])

            for _, stint in driver_stints.iterrows():
                lap_start = stint["lap_start"]
                compound = stint["compound"]

                color = {
                    "SOFT": "red",
                    "MEDIUM": "gold",
                    "HARD": "black"
                }.get(compound, "gray")

                plt.axvline(
                    x=lap_start,
                    linestyle="--",
                    alpha=0.7,
                    color=color
                )

                plt.text(
                    lap_start,
                    max(1, driver_data["position"].min() - 1),
                    compound,
                    rotation=90,
                    verticalalignment="bottom",
                    fontsize=8,
                    color=color
                )

    plt.gca().invert_yaxis()
    plt.xlabel("Lap Progression")
    plt.ylabel("Race Position")
    plt.title("Position Changes with Tyre Strategy")
    plt.legend()
    plt.tight_layout()
    plt.show()
