"""Reference weather client. Requires WEATHER_API_KEY only for live requests."""
import json
import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

SAMPLE = Path("sample_response.json")


def weather(city: str) -> dict:
    key = os.getenv("WEATHER_API_KEY")
    if not key and SAMPLE.exists(): return json.loads(SAMPLE.read_text())
    if not key: raise RuntimeError("Set WEATHER_API_KEY or add sample_response.json for offline mode.")
    query = urlencode({"q": city, "appid": key, "units": "metric"})
    with urlopen(f"https://api.openweathermap.org/data/2.5/weather?{query}", timeout=10) as response:
        return json.load(response)


def main() -> None:
    try:
        data = weather(input("City: "))
        print(f'{data["name"]}: {data["main"]["temp"]}°C, {data["weather"][0]["description"]}')
    except Exception as error:
        print(f"Could not get weather: {error}")


if __name__ == "__main__": main()
