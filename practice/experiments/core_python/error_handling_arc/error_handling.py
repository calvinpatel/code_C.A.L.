import requests

# Pick your poison — uncomment ONE at a time and run.

# url = "https://pokeapi.co/api/v2/pokemon/ditto"            # 1. works fine
# url = "https://pokeapi.co/api/v2/pokemon/notarealpokemon"  # 2. 404
# url = "https://pokeapi.co/api/v99/pokemon/ditto"           # 3. bad version → ?
# url = "https://this-domain-definitely-does-not-exist-cal.xyz"  # 4. DNS fail
# url = "https://httpbin.org/delay/10"                       # 5. slow (10s)
# url = "https://httpbin.org/status/500"                     # 6. server error 500
# url = "https://httpbin.org/status/503"                       # 7. service unavailable

response = requests.get(url)

print(f"Status code: {response.status_code}")
print(f"Body (first 200): {response.text[:200]}")