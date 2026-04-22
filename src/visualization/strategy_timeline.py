import matplotlib.pyplot as plt


def plot_strategy_timeline(stints_df, driver_map, selected_drivers=None):
    """
    Plot tyre strategy timeline for selected drivers.
    Each row = one driver
    Each bar = one stint
    """

    if stints_df.empty:
        print("No stint data available to plot.")
        return

    if selected_drivers is not None:
        filtered = stints_df[stints_df["driver_number"].isin(selected_drivers)].copy()
    else:
        filtered = stints_df.copy()

    drivers = filtered["driver_number"].drop_duplicates().tolist()

    plt.figure(figsize=(12, 4 + len(drivers)))

    for i, driver_number in enumerate(drivers):
        driver_stints = filtered[filtered["driver_number"] == driver_number]
        driver_name = driver_map.get(driver_number, str(driver_number))

        for _, stint in driver_stints.iterrows():
            lap_start = stint["lap_start"]
            stint_length = stint["stint_length"]
            compound = stint["compound"]

            color = {
                "SOFT": "red",
                "MEDIUM": "gold",
                "HARD": "black",
            }.get(compound, "gray")

            plt.barh(
                y=i,
                width=stint_length,
                left=lap_start,
                color=color,
                edgecolor="black",
                alpha=0.8,
            )

            plt.text(
                lap_start + stint_length / 2,
                i,
                compound,
                va="center",
                ha="center",
                color="white" if compound == "HARD" else "black",
                fontsize=9,
                fontweight="bold",
            )

    plt.yticks(
        range(len(drivers)),
        [driver_map.get(d, str(d)) for d in drivers]
    )
    plt.xlabel("Lap Number")
    plt.ylabel("Driver")
    plt.title("Tyre Strategy Timeline")
    plt.tight_layout()
    plt.show()
