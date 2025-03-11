import requests

# Constants
API_KEY = 'your_openweathermap_api_key'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_data(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def display_weather_data(data):
    if data['cod'] == 200:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description']

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather}")
    else:
        print("Error fetching weather data. Please check the location and try again.")

def main():
    location = input("Enter a city or ZIP code: ")
    weather_data = get_weather_data(location)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
