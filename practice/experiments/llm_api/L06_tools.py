import json
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"
T0 = {"temperature": 0}

LINES = [
    "BP 142/91, HR 88.",
    "Patient reports sharp low-back pain x3 days, worse when sitting.",
    "Start ibuprofen 400 mg TID; follow up in 2 weeks.",
]


CLASSIFY_TOOL = {
    "name": "classify_line",
    "description": ("Record which SOAP section one line of a clinical intake belongs to. "
                    "Use for every line; S = what the patient reports, O = measured or observed, "
                    "A = the clinician's assessment, P = the plan."),
    "input_schema": {
        "type": "object",
        "properties": {
            "reason": {"type": "string", "description": "One sentence: why this section."},
            "section": {"type": "string", "enum": ["S", "O", "A", "P"],
                        "description": "The SOAP section the line belongs to."},
        },
        "required": ["reason", "section"],
    },
}

VITALS_TOOL = {
    "name": "get_vitals",
    "description": ("Look up the most recent recorded vital signs for a patient by id. "
                    "Returns BP and HR as a short string. Use when a summary needs vitals "
                    "that are not present in the intake text."),
    "input_schema": {"type": "object",
                     "properties": {"patient_id": {"type": "string",
                                                   "description": "Chart id, e.g. P-1042"}},
                     "required": ["patient_id"]},
}
FAKE_CHART = {"P-1042": "BP 142/91, HR 88", "P-2077": "BP 118/76, HR 64"}


def get_vitals(patient_id: str) -> tuple[str, bool]:
    try:
        return FAKE_CHART[patient_id], False
    except KeyError:
        known = ", ".join(sorted(FAKE_CHART))
        return f"KeyError: no chart for {patient_id!r}. Known ids: {known}.", True


def dispatch(block) -> dict:
    """Run one tool_use block; return the tool_result block that answers it."""
    if block.name == "get_vitals":
        content, is_error = get_vitals(**block.input)
    else:
        content, is_error = f"Error: unknown tool {block.name!r}", True
    result = {"type": "tool_result", "tool_use_id": block.id, "content": content}
    if is_error:
        result["is_error"] = True
    return result


def stage_a():
    print("\n=== A: JSON in prose ===")
    for line in LINES:
        r = client.messages.create(model=MODEL, max_tokens=150, extra_body=T0,
                                   system=("Classify the intake line as one SOAP section. Reply with ONLY a JSON "
                                            "object {\"section\": ..., \"reason\": ...} where section is S, O, A, or P."),
                                   messages=[{"role": "user", "content": line}])
        text = r.content[0].text
        print("raw    :", repr(text))
        try:
            data = json.loads(text)
            print("parsed :", data, "| enum ok:", data.get("section") in ("S", "O", "A", "P"))
        except json.JSONDecodeError as e:
            print("json.loads ->", e)


def stage_b():
    print("\n=== B: forced tool_choice ===")
    for line in LINES:
        r = client.messages.create(model=MODEL, max_tokens=200, extra_body=T0,
                                   tools=[CLASSIFY_TOOL],
                                   tool_choice={"type": "tool", "name": "classify_line"},
                                   messages=[{"role": "user", "content": line}])
        types = [b.type for b in r.content]
        tool = next((b for b in r.content if b.type == "tool_use"), None)
        print(f"stop={r.stop_reason} len={len(r.content)} types={types}")
        print("input   :", tool.input if tool else None)


def run_loop(prompt: str, max_trips: int = 5):
    """The agent loop. Returns the final Message."""
    messages = [{"role": "user", "content": prompt}]
    resp = client.messages.create(model=MODEL, max_tokens=300, extra_body=T0,
                                  tools=[VITALS_TOOL], messages=messages)
    trips = 0
    while resp.stop_reason == "tool_use" and trips < max_trips:
        trips += 1
        print(f"  trip {trips}: stop_reason={resp.stop_reason}")
        messages.append({"role": "assistant", "content": resp.content})
        results = [dispatch(b) for b in resp.content if b.type == "tool_use"]
        messages.append({"role": "user", "content": results})
        resp = client.messages.create(model=MODEL, max_tokens=300, extra_body=T0,
                                      tools=[VITALS_TOOL], messages=messages)
    print(f"  final: stop_reason={resp.stop_reason}")
    return resp, messages

def stage_c():
    print("\n=== C: the loop ===")
    resp, _ = run_loop("Write the O line for patient P-1042.")
    text = next((b.text for b in resp.content if b.type == "text"), None)
    print("text   :", text)


def stage_d():
    print("\n=== D: the two 400s ===")
    messages = [{"role": "user", "content": "Write the O line for patient P-1042."}]
    r1 = client.messages.create(model=MODEL, max_tokens=300, extra_body=T0,
                                tools=[VITALS_TOOL], messages=messages)
    tool = next((b for b in r1.content if b.type == "tool_use"), None)
    if tool is None:
        print("model answered without a tool call; rerun D"); return

    bad_i = messages + [{"role": "assistant", "content": r1.content},
                        {"role": "user", "content": "That looked wrong, try again."}]
    try:
        client.messages.create(model=MODEL, max_tokens=100, extra_body=T0,
                               tools=[VITALS_TOOL], messages=bad_i)
        print("(i)  no error?!")
    except anthropic.BadRequestError as e:
        print("(i) ", e.status_code, e.body["error"]["message"])

    bad_ii = messages + [{"role": "assistant", "content": r1.content},
                         {"role": "user", "content": [
                             {"type": "text", "text": "Here are the results:"},
                             dispatch(tool)]}]
    try:
        client.messages.create(model=MODEL, max_tokens=100, extra_body=T0,
                               tools=[VITALS_TOOL], messages=bad_ii)
        print("(ii) no error?!")
    except anthropic.BadRequestError as e:
        print("(ii)", e.status_code, e.body["error"]["message"])


def stage_e():
    print("\n=== E: is_error ===")
    resp, messages = run_loop("Write the O line for patient P-9999.")
    text = next((b.text for b in resp.content if b.type == "text"), None)
    print("text   :", text)
    print("turns  :", len(messages) + 1)


if __name__ == "__main__":
    stage_a()
    stage_b()
    stage_c()
    stage_d()
    stage_e()
