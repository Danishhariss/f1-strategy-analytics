import pandas as pd


def clean_laps(laps_json):
    """
    Clean raw lap data from OpenF1 API
    """

    df = pd.DataFrame(laps_json)

    # Step 1: Keep only useful columns
    useful_cols = [
        'driver_number',
        'lap_number',
        'lap_duration'
    ]

    df = df[useful_cols]

    # Step 2: Remove missing values
    df = df.dropna()

    # Step 3: Convert types (important for analysis)
    df['lap_duration'] = pd.to_numeric(df['lap_duration'])

    return df
