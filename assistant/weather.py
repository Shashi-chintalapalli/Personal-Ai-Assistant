import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

def get_weather(city="Hyderabad"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return "Sorry, I couldn't fetch the weather."

    temp = response["main"]["temp"]
    desc = response["weather"][0]["description"]
    return f"The temperature in {city} is {temp}°C with {desc}."
