from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"

SYSTEM = "Classify the intake line as S, O, A, or P. Reply with the single letter only."
LINE = "Patient says the pharmacy kiosk read her BP as 150/95 last week."

def read(r):
    thinking, text = "", ""
    for b in r.content:
        match b.type:
            case "thinking": thinking += b.thinking
            case "text":     text += b.text
    return thinking, text

def run(label, **extra):
    r = client.messages.create(model=MODEL, max_tokens=2000, system=SYSTEM,
                               messages=[{"role": "user", "content": LINE}], **extra)
    thinking, text = read(r)
    print(f"[{label}] answer={text!r}  out={r.usage.output_tokens}  "
          f"details={r.usage.output_tokens_details}")
    if thinking:
        print("  thinking:", thinking[:300].replace("\n", " "), "…")
    print()

run("no-think")
run("think", thinking={"type": "enabled", "budget_tokens": 1024})
run("collide", thinking={"type": "enabled", "budget_tokens": 1024},
    extra_body={"temperature": 0})


COT_SYSTEM = ("Classify the intake line as S, O, A, or P. First reason briefly inside "
              "<reasoning> tags. Then, on its own line, give the single letter.")

r = client.messages.create(model=MODEL, max_tokens=300, system=COT_SYSTEM,
    messages=[{"role": "user", "content": LINE}], extra_body={"temperature": 0})
_, text = read(r)
print("blocks :", [b.type for b in r.content])
print("out    :", r.usage.output_tokens, r.usage.output_tokens_details)
print(text)