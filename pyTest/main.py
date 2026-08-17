def get_weather(temp) -> str:
    if temp > 20:
        return "hot"
    else:
        return "cold"
