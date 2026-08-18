def get_weather(temp: int | float) -> str:
    if temp > 20:
        return "hot"
    else:
        return "cold"
