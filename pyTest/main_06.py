import requests


def get_weather(city):
    response = requests.get(
        f"https://api.weather.com/v1/{city}"
    )  # we want to mock the api to test code locally
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch weather data")
