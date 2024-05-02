

import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = {
            "description": data['weather'][0]['description'],
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }
        return weather
    else:
        print("Error fetching weather data:", data['message'])
        return None

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "YOUR_API_KEY"  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key

    weather_data = get_weather(city, api_key)

    if weather_data:
        print("Weather in", city)
        print("Description:", weather_data["description"])
        print("Temperature:", weather_data["temperature"], "°C")
        print("Humidity:", weather_data["humidity"], "%")
        print("Wind Speed:", weather_data["wind_speed"], "m/s")
