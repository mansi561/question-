import requests

# Generate fake data for a person
response = requests.get('https://fakerapi.it/api/v1/persons')
data = response.json()[0]
print('Name:', data['first_name'], data['last_name'])
print('Email:', data['email'])
print('Phone:', data['phone'])

# Generate a fake image
response = requests.get('https://fakerapi.it/api/v1/images?_width=800')
data = response.json()
print('Image URL:', data['data'][0]['url'])

# Generate fake data for a place
response = requests.get('https://fakerapi.it/api/v1/places')
data = response.json()[0]
print('City:', data['city'])
print('Country:', data['country'])
print('Latitude:', data['latitude'])
print('Longitude:', data['longitude'])

# Generate fake data for a company
response = requests.get('https://fakerapi.it/api/v1/companies')
data = response.json()[0]
print('Company name:', data['name'])
print('Industry:', data['industry'])
print('Website:', data['url'])

# Generate fake data for an address
response = requests.get('https://fakerapi.it/api/v1/addresses')
data = response.json()[0]
print('Address:', data['address'])
print('City:', data['city'])
print('Postal code:', data['postcode'])
print('Country:', data['country'])
