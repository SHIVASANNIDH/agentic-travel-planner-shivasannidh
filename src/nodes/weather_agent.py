from src.tools import mock_weather

def weather_tool(city: str, days: int):
    return mock_weather(city, days)

