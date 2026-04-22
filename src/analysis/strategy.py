def average_pace(laps_df):
    """
    Calculate average lap time per driver
    Lower = faster driver
    """
    return laps_df.groupby('driver_number')['lap_duration'].mean()


def consistency(laps_df):
    """
    Calculate how consistent each driver is
    Lower std = more consistent (better control)
    """
    return laps_df.groupby('driver_number')['lap_duration'].std()


def performance_score(laps_df):
    """
    Combine speed + consistency into one metric
    (simple strategist scoring system)
    """

    avg = average_pace(laps_df)
    std = consistency(laps_df)

    score = avg + std  # lower is better overall

    return score.sort_values()


def fastest_driver(avg_pace):
    return avg_pace.idxmin(), avg_pace.min()


def most_consistent(consistency_series):
    return consistency_series.idxmin(), consistency_series.min()


def worst_consistency(consistency_series):
    return consistency_series.idxmax(), consistency_series.max()
