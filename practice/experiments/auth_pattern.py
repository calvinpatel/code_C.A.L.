import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("EXAMPLE_API_KEY")
base_url = os.getenv("POKEAPI_BASE_URL")

if not api_key:
    raise RuntimeError("EXAMPLE_API_KEY is not set. Check your .env file.")

# Construct headers — this is where the secret goes
headers = {
    "Authorization": f"Bearer {api_key}",
    "User-Agent": "code_C.A.L./0.1 (https://github.com/calvinpatel)",
}

# Now make a request with the headers
response = requests.get(
    f"{base_url}/pokemon/ditto",
    headers=headers,
    timeout=5,
)

print(f"Status: {response.status_code}")
print(f"Sent headers (echoed by requests):")
for key, value in response.request.headers.items():
    # Mask the Authorization value when printing
    if key.lower() == "authorization":
        value = f"{value[:10]}...{value[-4:]}"
    print(f"  {key}: {value}")

data = response.json()
print(f"\nGot Pokémon: {data['name']}")


print("\n=== Auth failure simulations ===\n")

# httpbin will return whatever status code you ask for
for status in [401, 403]:
    print(f"--- Simulating {status} ---")
    response = requests.get(
        f"https://httpbin.org/status/{status}",
        headers={"Authorization": "Bearer pretend-this-is-wrong"},
        timeout=5,
    )
    print(f"Status: {response.status_code}")
    print(f"Reason: {response.reason}")
    print()