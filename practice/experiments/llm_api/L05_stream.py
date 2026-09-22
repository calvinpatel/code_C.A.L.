import time
import anthropic
from anthropic.types import MessageParam
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"
SYSTEM = "You are a clinical documentation assistant."
PROMPT = ("Write a full SOAP note for: 34F, sharp low-back pain x3 days, "
          "worse sitting, no red flags. About 250 words.")
MSGS: list[MessageParam] = [{"role": "user", "content": PROMPT}]
KW = dict(model=MODEL, system=SYSTEM, messages=MSGS, extra_body={"temperature": 0.0})

def stamp(t0): return f"{(time.perf_counter() - t0) * 1000:6.0f}ms"


# ── (a) TTFT vs total ────────────────────────────────────────
print("--- (a) create() ---")
t0 = time.perf_counter()
r = client.messages.create(max_tokens=600, **KW)
print(f"{stamp(t0)}  returned | stop={r.stop_reason} out={r.usage.output_tokens}")

print("--- (a) stream() ---")
t0 = time.perf_counter()
first = None
with client.messages.stream(max_tokens=600, **KW) as stream:
    for text in stream.text_stream:
        if first is None:
            first = stamp(t0)
        print(text, end="", flush=True)
print()
print(f"{stamp(t0)}  finished | first text at {first}")


# ── (b) raw event sequence ───────────────────────────────────
print("--- (b) create(stream=True) ---")
seen = []
raw = client.messages.create(max_tokens=600, stream=True, **KW)
for event in raw:
    seen.append(event.type)
print(seen)


# ── (c) the ceiling ──────────────────────────────────────────
print("--- (c) max_tokens=25000, no stream ---")
try:
    r = client.messages.create(max_tokens=25000, **KW)
except ValueError as e:
    print(type(e).__name__, str(e)[:80], "...")