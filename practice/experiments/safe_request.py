import requests

def fetch_pokemon(name: str) -> dict | None:
    """
    Fetch a Pokémon by name. Returns a dict on success, None on failure.
    Logs the failure mode so you can see what happened.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print(f"❌ Timeout: {name} took too long to fetch")
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection error: couldn't reach the server for {name}")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP {e.response.status_code}: {name} → {e.response.reason}")
    except requests.exceptions.JSONDecodeError:
        print(f"❌ Server returned non-JSON for {name}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Unknown request error for {name}: {e}")

    return None


# Try it against the failure modes we already explored:
for name in ["ditto", "notarealpokemon", "pikachu"]:
    print(f"\nFetching: {name}")
    data = fetch_pokemon(name)
    if data:
        print(f"✓ Got {data['name']} (weight {data['weight']})")