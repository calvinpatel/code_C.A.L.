import requests

base_url = "https://pokeapi.co/api/v2/pokemon"
params = {
    "limit": 5,
    "offset": 10,
}

response = requests.get(base_url, params=params)
data = response.json()

print(f"Final URL: {response.url}")
print(f"Status:    {response.status_code}")
print(f"Got {len(data['results'])} pokemon back\n")
print(f"Total pokemon available: {data['count']}")
print(f"Next page URL:           {data['next']}")
print(f"Previous page URL:       {data['previous']}")

for entry in data["results"]:
    print(f"- {entry['name']}")
