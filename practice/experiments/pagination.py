import requests
import time

base_url = "https://pokeapi.co/api/v2/pokemon"
params = {"limit": 100, "offset": 0}

all_names = []
url = base_url
page_count = 0

start = time.perf_counter()

while url:
    response = requests.get(url, params=params if page_count == 0 else None)
    data = response.json()

    for entry in data["results"]:
        all_names.append(entry["name"])

    page_count += 1
    print(f"Page {page_count}: got {len(data['results'])} (total so far: {len(all_names)})")

    url = data["next"]

elapsed = time.perf_counter() - start

print(f"\nDONE — fetched {len(all_names)} pokemon across {page_count} pages")
print(f"First 5:  {all_names[:5]}")
print(f"Last 5:   {all_names[-5:]}")
print(f"Elapsed: {elapsed:.2f} seconds")