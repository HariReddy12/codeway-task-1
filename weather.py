import urllib.request
import json

def get_weather(api_key, location):
    # API endpoint for current weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        # Sending GET request to the API
        with urllib.request.urlopen(url) as response:
            # Reading and decoding JSON response
            data = json.loads(response.read().decode())
            
            # Extracting relevant weather information
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            description = data['weather'][0]['description']

            # Displaying weather information
            print(f"Weather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            print(f"Description: {description}")
    except Exception as e:
        print(f"Failed to retrieve weather data: {e}")

def main():
    # Prompting user for input
    location = input("Enter the name of a city or a zip code: ")

    # Enter your OpenWeatherMap API key here
    api_key = "YOUR_API_KEY"

    # Getting weather information
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
