import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

class Weather:
    def __init__(self, data):
        self.city = data["name"]
        self.temp = data["main"]["temp"]
        self.humidity = data["main"]["humidity"]
        self.description = data["weather"][0]["description"]

    def show(self):
        print(f"City:        {self.city}")
        print(f"Temperature: {self.temp} °C")
        print(f"Humidity:    {self.humidity}%")
        print(f"Conditions:  {self.description}")

url = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(url, params={"q": "Cairo", "appid": api_key, "units": "metric"})
Weather(response.json()).show()
