import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        # Extracting relevant weather information
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_data
    else:
        return None

def main():
    city = input("Enter the name of a city: ")
    weather = get_weather(city)
    if weather:
        print("\nWeather Forecast for", weather["city"])
        print("Temperature:", weather["temperature"], "°C")
        print("Humidity:", weather["humidity"], "%")
        print("Description:", weather["description"])
        print("Wind Speed:", weather["wind_speed"], "m/s")
    else:
        print("City not found or invalid input. Please try again.")

if __name__ == "__main__":
    main()
