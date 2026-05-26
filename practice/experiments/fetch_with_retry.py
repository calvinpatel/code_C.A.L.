import requests
import time


def fetch_with_retry(url: str, max_retries: int = 3, timeout: int = 5) -> dict | None:
    """Fetch a URL with exponential backoff on 5xx / connection failures."""

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            # Don't retry 4xx — those are YOUR fault, retrying won't help
            if 400 <= status < 500:
                print(f"❌ HTTP {status}: not retrying (client error)")
                return None
            # 5xx — server's fault, might be transient
            print(f"⚠️  HTTP {status} on attempt {attempt}/{max_retries}")

        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            print(f"⚠️  {type(e).__name__} on attempt {attempt}/{max_retries}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Unrecoverable: {e}")
            return None

        # If we got here, we're going to retry
        if attempt < max_retries:
            wait = 2 ** (attempt - 1)  # 1, 2, 4, 8 seconds
            print(f"    waiting {wait}s before retry...")
            time.sleep(wait)

    print(f"❌ Gave up after {max_retries} attempts")
    return None


# Test against httpbin's 503 endpoint — should retry, then give up
print("=== Test 1: persistent 503 (will retry then give up) ===")
fetch_with_retry("https://httpbin.org/status/503")

print("\n=== Test 2: 404 (should NOT retry — client error) ===")
fetch_with_retry("https://pokeapi.co/api/v2/pokemon/notarealpokemon")

print("\n=== Test 3: happy path ===")
result = fetch_with_retry("https://pokeapi.co/api/v2/pokemon/ditto")
if result:
    print(f"✓ Got {result['name']}")