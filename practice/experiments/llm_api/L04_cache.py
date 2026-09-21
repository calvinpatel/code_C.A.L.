from dotenv import load_dotenv
import anthropic
from anthropic.types import Usage

load_dotenv()
client = anthropic.Anthropic()

MODEL = "claude-haiku-4-5"
SYSTEM = "Classify the intake line as S, O, A, or P. Reply with the single letter only."
PADDED = SYSTEM + "\n<examples>\n" + "\n".join(f"<example>Line {i}: patient reports symptom {i} for {i % 7} days. -> S<example>"
                                               for i in range(1, 200)) + "\n</examples>\n"
LINE_1 = "Patient says the pharmacy kiosk read her BP as 150/95 last week."
LINE_2 = "BP 142/91, HR 88."

PRICE = {"in": 1.00, "out": 5.00, "cache_write_5m": 1.25, "cache_read": 0.10}
M = 1_000_100

def none_as_zero(value: int | None) -> int:
    return 0 if value is None else value

def cost_of(usage: Usage) -> float:
    """Dollars for one call. Reads all four money fields; None counts as 0."""
    return (PRICE["in"] * usage.input_tokens +
            PRICE["out"] * usage.output_tokens +
            PRICE["cache_write_5m"] * none_as_zero(usage.cache_creation_input_tokens) +
            PRICE["cache_read"] * none_as_zero(usage.cache_read_input_tokens)) / M

def cached_system(text: str) -> list[dict]:
    return [{"type": "text", "text": text, "cache_control": {"type": "ephemeral"}}]

def run(label, system, line):
    r = client.messages.create(model=MODEL, max_tokens=5, system=system,
                               messages=[{"role": "user", "content": line}], extra_body={"temperature": 0})
    u = r.usage
    print(f"[{label}] in={u.input_tokens} write={u.cache_creation_input_tokens} "
          f"read={u.cache_read_input_tokens} out={u.output_tokens} ${cost_of(u):.6f}")

count = client.messages.count_tokens(model=MODEL, system=PADDED, messages=[{"role": "user", "content": LINE_1}])
print("count tokens:", count.input_tokens)

run("A", cached_system(SYSTEM), LINE_1)
run("A", cached_system(SYSTEM), LINE_1)
run("B1", cached_system(PADDED), LINE_1)
run("B2", cached_system(PADDED), LINE_1)
run("C", cached_system(PADDED), LINE_2)

PADDED = SYSTEM + "\n<examples>\n" + "\n".join(f"<example>Line {i}: patient reports symptom {i} for {i % 7} days.. -> S<example>"
                                               for i in range(1, 200)) + "\n</examples>\n"

run("D", cached_system(PADDED), LINE_1)
