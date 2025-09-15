
import requests

city = input("Enter the city name: ")

# Your API key from OpenWeatherMap
api_key ="92dc956b33732943e90947b9c2eacc44"


base_url = "http://api.openweathermap.org/data/2.5/weather"

# Parameters for the API call
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"  # Use "imperial" for Fahrenheit
}

# Make the request
response = requests.get(base_url, params=params)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print("\n🌦️ Weather Report for", city)
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"].capitalize())
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("\n⚠️ Error:", response.status_code)
    print("Details:", response.json().get("message", "Something went wrong."))



