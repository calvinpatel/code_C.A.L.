from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"

SYSTEM = "Summarize the intake into one line of S (Subjective). Never add facts."
INTAKE = "<intake>\nSharp low-back pain x3 days, worse when sitting.\n</intake>"

def run(label, **extra):
    outs = []
    for i in range(5):
        r = client.messages.create(model=MODEL, max_tokens=60, system=SYSTEM,
                                   messages=[{"role": "user", "content": INTAKE}], **extra)
        outs.append(r.content[0].text)
        print(f"[{label}-{i}] {r.content[0].text!r}")
    print(f"{label}: {len(set(outs))} distinct of 5\n")

run("default")
run("zero", extra_body={"temperature": 0})