import requests

BASE_URL = "https://api.openf1.org/v1"


def get_sessions(year=None, country=None, session_name=None):
    params = {}

    if year is not None:
        params["year"] = year
    if country is not None:
        params["country_name"] = country
    if session_name is not None:
        params["session_name"] = session_name

    response = requests.get(f"{BASE_URL}/sessions", params=params)
    response.raise_for_status()
    return response.json()


def get_laps(session_key):
    response = requests.get(f"{BASE_URL}/laps", params={"session_key": session_key})
    response.raise_for_status()
    return response.json()


def get_drivers(session_key):
    response = requests.get(f"{BASE_URL}/drivers", params={"session_key": session_key})
    response.raise_for_status()
    return response.json()


def get_positions(session_key):
    response = requests.get(f"{BASE_URL}/position", params={"session_key": session_key})
    response.raise_for_status()
    return response.json()


def get_pit_stops(session_key):
    response = requests.get(f"{BASE_URL}/pit", params={"session_key": session_key})

    if response.status_code == 404:
        print("\nPit stop data is not available for this session.")
        return []

    response.raise_for_status()
    return response.json()


def get_stints(session_key):
    response = requests.get(f"{BASE_URL}/stints", params={"session_key": session_key})
    response.raise_for_status()
    return response.json()
