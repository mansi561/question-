import requests

# Enter your API key from BehindTheName
API_KEY = 'your_api_key_here'

# Define the name you want to search for
name = 'John'

# Make a request to the API to get information about the name
url = f'https://www.behindthename.com/api/lookup.json?name={name}&key={API_KEY}'
response = requests.get(url).json()

# Check if the name is male or female
if response['gender'] == 'm':
    color = 'blue'  # Male names will have a blue background
elif response['gender'] == 'f':
    color = 'pink'  # Female names will have a pink background
else:
    color = 'gray'  # Names with unknown gender will have a gray background

# Display information about the name and indicate its gender with a colored background
print(f"Name: {response['name']} ({response['gender']})")
print(f"Meaning: {response['meaning']}")
print(f"Usage: {', '.join(response['usage'])}")
print(f"Popularity: {response['popularity']}")
 
