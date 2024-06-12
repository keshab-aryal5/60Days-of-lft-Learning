import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
    else:
        print("City not found.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "d038dafe86e4cb38bca2a44ddcac2078"
  # Replace with your actual OpenWeatherMap API key
    get_weather(city_name, api_key)
