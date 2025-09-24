from tabulate import tabulate

def itinerary_tool(pois, weather):
    itinerary = []
    for i, day_weather in enumerate(weather, start=1):
        morning = pois[(i*2 - 2) % len(pois)]["name"]
        afternoon = pois[(i*2 - 1) % len(pois)]["name"]
        evening = "Free exploration"
        itinerary.append([
            f"Day {i}",
            morning,
            afternoon,
            evening,
            f"{day_weather['condition']} {day_weather['temp']}"
        ])
    return tabulate(itinerary, headers=["Day", "Morning", "Afternoon", "Evening", "Weather"], tablefmt="grid")
