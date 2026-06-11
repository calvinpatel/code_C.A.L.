import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY is not set. Check your .env file.")

url = "https://api.anthropic.com/v1/messages"

headers = {
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}

payload = {
    "model": "claude-haiku-4-5-20251001",
    "max_tokens": 200,
    "messages": [
        {"role": "user", "content": "In one sentence, why is Ditto the most underrated Pokémon?"}
    ],
}

try:
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()

    print("=== Full response structure ===")
    print(f"Model:        {data['model']}")
    print(f"Stop reason:  {data['stop_reason']}")
    print(f"Tokens in:    {data['usage']['input_tokens']}")
    print(f"Tokens out:   {data['usage']['output_tokens']}")
    print(f"\n=== Claude says ===")
    print(data["content"][0]["text"])

except requests.exceptions.HTTPError as e:
    print(f"❌ HTTP {e.response.status_code}: {e.response.text}")
except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")