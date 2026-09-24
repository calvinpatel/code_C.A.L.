import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"
THINKING = {"type": "enabled", "budget_tokens": 1024}
VITALS_TOOL = {
    "name": "get_vitals",
    "description": "Fetch the most recent vital signs for a patient by chart ID.",
    "input_schema": {
        "type": "object",
        "properties": {
            "patient_id": {"type": "string", "description": "Chart ID, e.g. P-1042."},
        },
        "required": ["patient_id"],
    },
}
ASK = "What were the latest vitals for patient P-1042?"
FAKE_CHART = {"P-1042": "BP 142/91, HR 88, T 99.1 F, SpO2 96%"}

# ---- call 1: stream it, fold thinking for display ----
thinking_parts: list[str] = []
with client.messages.stream(model=MODEL, max_tokens=2000, thinking=THINKING,
        tools=[VITALS_TOOL], messages=[{"role": "user", "content": ASK}]) as stream:
    for ev in stream:
        if ev.type == "content_block_delta":
            d = ev.delta
            match d.type:
                case "thinking_delta":
                    thinking_parts.append(d.thinking)
                    print(f"[{ev.index}] thinking_delta   {len(d.thinking):4} chars")
                case "signature_delta":
                    print(f"[{ev.index}] signature_delta  {len(d.signature):4} chars")
                case "input_json_delta":
                    print(f"[{ev.index}] input_json_delta {d.partial_json!r}")
        elif ev.type == "content_block_stop":
            print(f"[{ev.index}] stop")
    r1 = stream.get_final_message()

tool = next((b for b in r1.content if b.type == "tool_use"), None)
assert tool is not None, "model answered without calling the tool"
tool_result = {"type": "tool_result", "tool_use_id": tool.id,
               "content": FAKE_CHART[tool.input["patient_id"]]}

# ---- call 2: two ways to send the assistant turn back ----
arms = {
    "display fold": [{"type": "thinking", "thinking": "".join(thinking_parts)}, tool],
    "final.content": r1.content,
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
        print(f"{label:13} | 200 | in={r2.usage.input_tokens:4} | {[b.type for b in r2.content]}")
    except anthropic.BadRequestError as e:
        print(f"{label:13} | 400 | {e.body['error']['message']}")