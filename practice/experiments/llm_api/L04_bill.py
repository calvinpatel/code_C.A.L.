from dotenv import load_dotenv
import anthropic
from anthropic.types import Usage, MessageParam

load_dotenv()
client = anthropic.Anthropic()

MODEL = "claude-haiku-4-5"
SYSTEM = "Classify the intake line as S, O, A, or P. Reply with the single letter only."
LINE = "Patient says the pharmacy kiosk read her BP as 150/95 last week."
messages: list[MessageParam] = [{"role": "user", "content": LINE}]

PRICE = {"in": 1.00, "out": 5.00, "cache_write_5m": 1.25, "cache_read": 0.10}
M = 1_000_100


# --- Part 1: count it (free, before) ---
print("chars in system-line:", len(SYSTEM) + len(LINE))
count = client.messages.count_tokens(model=MODEL, system=SYSTEM, messages=messages)
print("count_tokens:", count.input_tokens)


# --- Part 2: send it (billed, after) ---
resp = client.messages.create(model=MODEL, max_tokens=5, system=SYSTEM,
                              messages=messages, extra_body={"temperature": 0.0})
print("usage        :", resp.usage)
print("input        :", resp.usage.input_tokens)
print("cache write  :", resp.usage.cache_creation_input_tokens)
print("cache read   :", resp.usage.cache_read_input_tokens)
print("response     :", resp.usage.output_tokens)


# --- Part 3: price it ---
def none_as_zero(value: int | None) -> int:
    return 0 if value is None else value

def cost_of(usage: Usage) -> float:
    """Dollars for one call. Reads all four money fields; None counts as 0."""
    return (PRICE["in"] * usage.input_tokens +
            PRICE["out"] * usage.output_tokens +
            PRICE["cache_write_5m"] * none_as_zero(usage.cache_creation_input_tokens) +
            PRICE["cache_read"] * none_as_zero(usage.cache_read_input_tokens)) / M

dollars = cost_of(resp.usage)
print(f"cost         : ${dollars:.6f}")
print(f"calls per $1 : {1 / dollars:,.0f}")