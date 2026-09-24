from dotenv import load_dotenv
import anthropic
from pydantic import BaseModel, ValidationError

load_dotenv()
client = anthropic.Anthropic()

SYSTEM = (
    "You label lines of clinical intake notes. "
    "House style: always write the section's full name — "
    "Subjective, Objective, Assessment, or Plan. Never abbreviate."
)
LINE = "BP 142/91, HR 88."

def classify_tool(strict: bool) -> dict:
    tool = {
        "name": "classify_line",
        "description": "Record which SOAP section one line of a clinical intake belongs to.",
        "input_schema": {
            "type": "object",
            "properties": {
                "section": {"type": "string", "enum": ["S", "O", "A", "P"]},
            },
            "required": ["section"],
            "additionalProperties": False,
        },
    }
    if strict:
        tool["strict"] = True
    return tool

# for strict in (False, True):
#     sections = []
#     for _ in range(5):
#         resp = client.messages.create(
#             model="claude-haiku-4-5",
#             max_tokens=100,
#             system=SYSTEM,
#             tools=[classify_tool(strict)],
#             tool_choice={"type": "tool", "name": "classify_line"},
#             messages=[{"role": "user", "content": LINE}],
#         )
#         tool = next((b for b in resp.content if b.type == "tool_use"), None)
#         sections.append(tool.input.get("section"))
#     print(f"strict={strict}  sections={sections}")

VITALS_SYSTEM = (
    "You extract vital signs from one line of a clinical intake note. "
    "Record only values written in the line. If a vital is not documented, "
    "set its field to null. Never estimate or invent a value."
)

def vitals_tool(strict: bool) -> dict:
    tool = {
        "name": "record_vitals",
        "description": "Record the vital signs documented in one line of a clinical intake note.",
        "input_schema": {
            "type": "object",
            "properties": {
                "heart_rate": {"type": "integer", "description": "Heart rate in beats per minute."},
                "temp_f": {"type": ["number", "null"], "description": "Body temperature in degrees Fahrenheit."},
            },
            "required": ["heart_rate", "temp_f"],
            "additionalProperties": False,
        },
    }
    if strict:
        tool["strict"] = True
    return tool

# for strict in (False, True):
#     for _ in range(5):
#         resp = client.messages.create(
#             model="claude-haiku-4-5",
#             max_tokens=100,
#             system=VITALS_SYSTEM,
#             tools=[vitals_tool(strict)],
#             tool_choice={"type": "tool", "name": "record_vitals"},
#             messages=[{"role": "user", "content": LINE}],
#         )
#         tool = next((b for b in resp.content if b.type == "tool_use"), None)
#         print(f"strict={strict}  input={tool.input}  temp_f={tool.input.get('temp_f', 'MISSING')}")

# try:
#     resp = client.messages.create(
#         model="claude-opus-5-5",
#         max_tokens=200,
#         system=VITALS_SYSTEM,
#         tools=[vitals_tool(strict=True)],
#         tool_choice={"type": "tool", "name": "record_vitals"},
#         messages=[{"role": "user", "content": LINE}],
#     )
#     tool = next((b for b in resp.content if b.type == "tool_use"), None)
#     print("stop:", resp.stop_reason, " input:", tool.input if tool else None)
# except anthropic.BadRequestError as e:
#     print(e.status_code, e.body["error"]["message"])

class Vitals(BaseModel):
    heart_rate: int
    temp_f: float | None

# for model in ("claude-haiku-4-5", "claude-opus-5-5"):
#     resp = client.messages.parse(
#         model=model,
#         max_tokens=2000,
#         system=VITALS_SYSTEM,
#         messages=[{"role": "user", "content": LINE}],
#         output_format=Vitals
#     )
#     block_type = [b.type for b in resp.content]
#     print(f"model={model}, stop_reason={resp.stop_reason}, type={block_type}, output={repr(resp.parsed_output)}")

try:
    resp = client.messages.parse(
        model="claude-haiku-4-5",
        max_tokens=5,
        system=VITALS_SYSTEM,
        messages=[{"role": "user", "content": LINE}],
        output_format=Vitals,
    )
    print("returned:", resp.stop_reason, repr(resp.parsed_output))
except ValidationError as e:
    print("raised:", type(e).__name__, "|", str(e).splitlines()[1], "|")