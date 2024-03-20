import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    data = response.json()
    print(f"{data['weather']}")
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to retrieve weather information.")

def main():
    api_key = "d885aa1d783fd13a55050afeef620fcb"  # Replace 'YOUR_API_KEY' with your actual API key
    city = input("Enter the city name: ")
    get_weather(city, api_key)

if _name_ == "_main_":
    main()
