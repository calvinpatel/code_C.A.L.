import requests

pokemon_name = "pikachu"

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
response = requests.get(url)
data = response.json()

print(f"Name:   {data['name']}")
print(f"Height: {data['height']}")
print(f"Weight: {data['weight']}")
print(f"Types:  {[t['type']['name'] for t in data['types']]}")