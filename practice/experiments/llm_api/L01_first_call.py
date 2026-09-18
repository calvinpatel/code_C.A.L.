import os
from dotenv import load_dotenv
import anthropic
from anthropic.types import MessageParam

load_dotenv()           # .env -> os.environ
print("key loaded:", os.environ.get("ANTHROPIC_API_KEY", "MISSING")[:10])  # print first 10 characters of the key
client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY from os.environ

# ── RUN A: the first call ──────────────────────────────────────
resp = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[{"role": "user", "content": "Hi, I'm Cal. Say hello in one line."}],
)
print("A text       :", resp.content[0].text)
print("A blocks     :", len(resp.content))
print("A stop reason:", resp.stop_reason)
print("A model      :", resp.model)
print("A usage      :", resp.usage.input_tokens, "in /", resp.usage.output_tokens, "out")


# ── RUN B: does it remember? ───────────────────────────────────
r1 = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=50,
    messages=[{"role": "user", "content": "My name is Cal. Please remember it."}],
)
print("B1:", r1.content[0].text)

r2 = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=50,
    messages=[{"role": "user", "content": "What is my name?"}],
)
print("B2:", r2.content[0].text)


# ── RUN C: hit the ceiling ─────────────────────────────────────
r3 = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=5,
    messages=[{"role": "user", "content": "Explain what a SOAP note is."}],
)
print("C text       :", repr(r3.content[0].text))
print("C stop_reason:", r3.stop_reason)
print("C usage      :", r3.usage.output_tokens, "out")

for m in client.models.list(): print(m.id)


# ── RUN D: carry the transcript ────────────────────────────────
history: list[MessageParam] = [{"role": "user", "content": "My name is Cal. Please remember it."}]
d1 = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=50,
    messages=history,
)
history.append({"role": "assistant", "content": d1.content})
history.append({"role": "user", "content": "What is my name?"})
d2 = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=50,
    messages=history,
)
print("D2 text:", d2.content[0].text)
print("D2 in:", d2.usage.input_tokens, "| B2 in:", r2.usage.input_tokens)