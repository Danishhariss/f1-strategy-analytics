from src.api.openf1_api import (
    get_sessions,
    get_laps,
    get_drivers,
    get_positions,
    get_pit_stops,
    get_stints,
)
from src.processing.clean_laps import clean_laps
from src.processing.clean_positions import clean_positions
from src.processing.clean_pit_stops import clean_pit_stops
from src.processing.clean_stints import clean_stints
from src.analysis.strategy import (
    average_pace,
    consistency,
    fastest_driver,
    most_consistent,
    worst_consistency,
)
from src.analysis.position_analysis import position_change_summary
from src.analysis.pit_stop_analysis import summarize_pit_stops
from src.analysis.stint_analysis import (
    summarize_stints,
    get_selected_driver_stints,
    build_strategy_story,
)
from src.visualization.position_chart import plot_position_trends
from src.visualization.strategy_timeline import plot_strategy_timeline


def main():
    sessions = get_sessions(year=2023, country="Bahrain", session_name="Race")

    if not sessions:
        print("No session found!")
        return

    session = sessions[0]
    session_key = session["session_key"]

    print("Session:", session["session_name"])
    print("Year:", session["year"])
    print("Country:", session["country_name"])

    # =========================
    # FETCH DATA
    # =========================
    laps_json = get_laps(session_key)
    drivers_json = get_drivers(session_key)
    positions_json = get_positions(session_key)
    pit_json = get_pit_stops(session_key)
    stints_json = get_stints(session_key)

    # =========================
    # CLEAN DATA
    # =========================
    laps = clean_laps(laps_json)
    positions = clean_positions(positions_json)
    pit_stops = clean_pit_stops(pit_json)
    stints = clean_stints(stints_json)

    # =========================
    # DRIVER MAP
    # =========================
    driver_map = {
        d["driver_number"]: d.get("full_name")
        or d.get("name_acronym")
        or str(d["driver_number"])
        for d in drivers_json
    }

    print("\nAvailable drivers:")
    for number, name in sorted(driver_map.items()):
        print(f"{number}: {name}")

    # =========================
    # USER MODE (SINGLE / MULTI)
    # =========================
    mode = input("\nChoose mode ('single' or 'multi'): ").strip().lower()

    if mode == "single":
        selected_driver = int(input("Enter one driver number: ").strip())

        if selected_driver not in driver_map:
            print("Invalid driver number selected.")
            return

        selected_drivers = [selected_driver]

    elif mode == "multi":
        raw_input_drivers = input(
            "Enter driver numbers separated by commas (e.g. 1,11,14): "
        ).strip()

        try:
            selected_drivers = [
                int(x.strip()) for x in raw_input_drivers.split(",") if x.strip()
            ]
        except ValueError:
            print("Invalid input. Please enter only numbers separated by commas.")
            return

        invalid = [d for d in selected_drivers if d not in driver_map]
        if invalid:
            print(f"Invalid driver numbers: {invalid}")
            return

    else:
        print("Invalid mode selected.")
        return

    # =========================
    # STRATEGY INSIGHTS
    # =========================
    avg_pace = average_pace(laps).rename(index=driver_map).sort_values()
    cons = consistency(laps).rename(index=driver_map).sort_values()

    fast_driver, fast_time = fastest_driver(avg_pace)
    consistent_driver, consistent_val = most_consistent(cons)
    worst_driver, worst_val = worst_consistency(cons)

    print("\n=== SIMPLE RACE INSIGHTS ===")
    print(f"Fastest overall pace: {fast_driver} ({fast_time:.2f}s average lap)")
    print(f"Most consistent pace: {consistent_driver} ({consistent_val:.2f})")
    print(f"Least consistent pace: {worst_driver} ({worst_val:.2f})")

    # =========================
    # POSITION SUMMARY
    # =========================
    position_summary = position_change_summary(positions).rename(index=driver_map)

    print("\n=== POSITION CHANGES ===")
    print(position_summary)

    # =========================
    # PIT STOP SUMMARY
    # =========================
    pit_summary = summarize_pit_stops(pit_stops)

    if not pit_summary.empty:
        pit_summary = pit_summary.rename(index=driver_map)
        print("\n=== PIT STOP SUMMARY ===")
        print(pit_summary)
    else:
        print("\nNo pit stop data found for this session.")

    # =========================
    # STINT SUMMARY
    # =========================
    stints_summary = summarize_stints(stints)

    if not stints_summary.empty:
        stints_summary = stints_summary.rename(index=driver_map)

        print("\n=== TYRE STRATEGY SUMMARY ===")
        print(stints_summary)

        print("\n=== SELECTED DRIVER TYRE PLAN ===")
        for driver in selected_drivers:
            driver_name = driver_map[driver]
            driver_stints = get_selected_driver_stints(stints, driver)

            print(f"\n--- {driver_name} ---")
            print(
                driver_stints[
                    ["stint_number", "compound", "lap_start", "lap_end", "stint_length"]
                ]
            )

            story = build_strategy_story(driver_stints, driver_name)
            print("\nStrategy Summary:")
            print(story)

    else:
        print("\nNo stint data found for this session.")

    # =========================
    # VISUALIZATIONS
    # =========================

    # 1) Position chart first
    plot_position_trends(
        positions,
        driver_map,
        selected_drivers=selected_drivers,
        stints_df=stints,
    )

    # 2) Strategy timeline second
    plot_strategy_timeline(
        stints,
        driver_map,
        selected_drivers=selected_drivers,
    )


if __name__ == "__main__":
    main()
