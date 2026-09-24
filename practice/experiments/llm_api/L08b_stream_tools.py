from dotenv import load_dotenv
import json
import anthropic

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"
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

raw = client.messages.create(model=MODEL, max_tokens=500, stream=True,
                             tools=[VITALS_TOOL], messages=[{"role": "user", "content": ASK}])

parts: dict[int, list[str]] = {}
for ev in raw:
    match ev.type:
        case "content_block_start":
            block = ev.content_block
            print(f"[{ev.index}] start {block.type}", block.input if block.type == "tool_use" else "")
            if block.type == "tool_use":
                parts[ev.index] = []
        case "content_block_delta":
            if ev.delta.type == "input_json_delta":
                print(f"[{ev.index}] frag {ev.delta.partial_json!r}")
                parts[ev.index].append(ev.delta.partial_json)
        case "content_block_stop":
            if ev.index in parts:
                text = "".join(parts[ev.index])
                print(f"[{ev.index}] stop -> {json.loads(text)}")
        case "message_delta":
            print("stop_reason: ", ev.delta.stop_reason)
            print("stop_details:", ev.delta.stop_details)
            print("container:   ", ev.delta.container)
        case _:
            pass