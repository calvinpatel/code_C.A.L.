import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"
THINKING = {"type": "enabled", "budget_tokens": 1024}
VITALS_TOOL = {
    "name": "get_vitals",
    "description": "Look up the most recent vital signs for a patient by id.",
    "input_schema": {"type": "object",
                     "properties": {"patient_id": {"type": "string"}},
                     "required": ["patient_id"]},
}
FAKE_CHART = {"P-1042": "BP 142/91, HR 88"}
ASK = "Write the O line for patient P-1042."

r1 = client.messages.create(model=MODEL, max_tokens=2000, thinking=THINKING,
    tools=[VITALS_TOOL], messages=[{"role": "user", "content": ASK}])
thinking = next((b for b in r1.content if b.type == "thinking"), None)
tool = next((b for b in r1.content if b.type == "tool_use"), None)
tool_result = {"type": "tool_result", "tool_use_id": tool.id,
               "content": FAKE_CHART[tool.input["patient_id"]]}

scrubbed_text = thinking.thinking.replace("P-1042", "[ID]")
print("scrub changed the text:", scrubbed_text != thinking.thinking)

arms = {
    "whole":    r1.content,
    "scrubbed": [{"type": "thinking", "thinking": scrubbed_text,
                  "signature": thinking.signature}, tool],
    "sig cut":  [{"type": "thinking", "thinking": thinking.thinking,
                  "signature": thinking.signature[:-10]}, tool],
}
for label, assistant_content in arms.items():
    messages = [
        {"role": "user", "content": ASK},
        {"role": "assistant", "content": assistant_content},
        {"role": "user", "content": [tool_result]},
    ]
    try:
        r2 = client.messages.create(model=MODEL, max_tokens=2000, thinking=THINKING,
                                    tools=[VITALS_TOOL], messages=messages)
        print(f"{label:8} | 200 | in={r2.usage.input_tokens:4} | {[b.type for b in r2.content]}")
    except anthropic.BadRequestError as e:
        print(f"{label:8} | {e.status_code} | {e.body['error']['message']}")