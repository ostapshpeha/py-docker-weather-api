import os
import sys

import requests


def get_weather() -> None:
    secret_key = os.getenv("API_KEY")
    if not secret_key:
        print(
            "CRITICAL ERROR: API_KEY is missing in environment variables!",
            file=sys.stderr
        )
        sys.exit(1)

    location = "Paris"
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": secret_key,
        "q": location,
        "days": 7,
        "aqi": "no",
        "alerts": "no"
    }

    print(f"Fetching weather for {location}...", flush=True)

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        current_temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(
            f"SUCCESS: Weather in {location}: {current_temp}°C, {condition}",
            flush=True
        )

    except requests.exceptions.RequestException as e:
        print(f"REQUEST FAILED: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
