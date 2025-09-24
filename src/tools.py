import random
from datetime import datetime, timedelta

def mock_weather(city: str, days: int):
    conditions = ["Sunny", "Cloudy", "Rainy", "Clear", "Hot", "Mild"]
    today = datetime.now()
    forecast = []
    for i in range(days):
        forecast.append({
            "date": (today + timedelta(days=i)).strftime("%Y-%m-%d"),
            "condition": random.choice(conditions),
            "temp": f"{random.randint(20, 35)}°C"
        })
    return forecast


def mock_pois(city: str):
    city_pois = {
        "new delhi": [
            {"name": "Red Fort", "desc": "Historic site"},
            {"name": "India Gate", "desc": "Famous landmark"},
            {"name": "Qutub Minar", "desc": "UNESCO monument"},
            {"name": "Lotus Temple", "desc": "Modern temple"},
            {"name": "Connaught Place", "desc": "Shopping & food hub"},
        ],
        "paris": [
            {"name": "Eiffel Tower", "desc": "Iconic landmark"},
            {"name": "Louvre Museum", "desc": "World’s largest art museum"},
            {"name": "Notre Dame", "desc": "Historic cathedral"},
            {"name": "Champs-Élysées", "desc": "Shopping & cafes"},
        ]
    }
    return city_pois.get(city.lower(), [{"name": "Central Park", "desc": "Famous park"}])
