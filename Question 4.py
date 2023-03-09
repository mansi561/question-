import requests

# Enter your OpenWeatherMap API key here
api_key = "your_api_key"

# Enter the character name and species here
name = "Morty"
species = "human"

# Construct the API endpoint URL with the parameters
url = f"https://api.openweathermap.org/data/2.5/weather?q={name},{species}&appid={api_key}"

# Make the API request and get the JSON response
response = requests.get(url)
data = response.json()

# Extract the relevant information from the JSON response
temperature = data['main']['temp']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']

# Print the information
print(f"{name} ({species}) - Temperature: {temperature}K, Humidity: {humidity}%, Wind Speed: {wind_speed}m/s")
