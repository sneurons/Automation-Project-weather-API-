# Weather API  # Automation
# api key :e71d3b09db9edc9c5f9f319746ba6f7e

import requests

API_KEY = "e71d3b09db9edc9c5f9f319746ba6f7e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"  # base url :where we want the data from

city = input("Enter a city name:  ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred")
