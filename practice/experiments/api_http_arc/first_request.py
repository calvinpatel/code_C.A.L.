import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(response)
print(type(response))
print(response.status_code)

print("\n--- response.text (raw body) ---")
print(response.text[:200])  # just the first 200 chars so we don't drown

print("\n--- response.json() (parsed) ---")
data = response.json()
print(type(data))
print(data["name"])
print(data["weight"])
print(data["height"])

print("\n--- top-level keys ---")
print(list(data.keys()))

print("\n--- one key explored ---")
print(data["abilities"])

import json

print("\n--- abilities, prettified ---")
print(json.dumps(data["abilities"], indent=2))

print(data["abilities"][1])                       # what is this?
print(data["abilities"][1]["ability"]["name"])    # and this?
print(len(data["abilities"]))                     # how many abilities does Ditto have?

print("\n--- Ditto's abilities (formatted) ---")
for entry in data["abilities"]:
    name = entry["ability"]["name"]
    hidden = entry["is_hidden"]
    label = " (hidden)" if hidden else ""
    print(f"- {name}{label}")

print("\n--- stats (raw) ---")
print(data["stats"])
print(type(data["stats"]))
print(len(data["stats"]))

print("\n--- stats (prettified) ---")
print(json.dumps(data["stats"], indent=2))

print("\n--- Ditto's stats (formatted) ---")
for entry in data["stats"]:
    name = entry["stat"]["name"]
    value = entry["base_stat"]
    print(f"{name}: {value}")

print("\n--- types (prettified) ---")
print(json.dumps(data["types"], indent=2))

print("\n--- Ditto's types ---")
for entry in data["types"]:
    print(f"- {entry['type']['name']}")

print("\n--- sprites (raw) ---")
print(data["sprites"])

print("\n--- sprites (prettified) ---")
print(json.dumps(data["sprites"], indent=2))
print(type(data["sprites"]))

print("\n--- Ditto's main sprites ---")
sprites = data["sprites"]
print(f"Front default:  {sprites['front_default']}")
print(f"Back default:   {sprites['back_default']}")
print(f"Front shiny:    {sprites['front_shiny']}")
print(f"Back shiny:     {sprites['back_shiny']}")