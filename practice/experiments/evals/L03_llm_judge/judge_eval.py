from typing import Literal
from dotenv import load_dotenv
import anthropic
from pydantic import BaseModel

load_dotenv()
client = anthropic.Anthropic()

SOURCE = ("Discharge: amoxicillin 1 g by mouth three times daily for 5 days. "
          "Return to the ED if your oxygen saturation falls below 92% or your "
          "shortness of breath worsens.")

OUTPUTS = {
    "A": ("Take amoxicillin 1 g three times a day for 5 days. Come back to the ER "
          "if your oxygen drops below 92% or you get more short of breath."),
    "G": ("Take amoxicillin 1 g three times a day for 5 days. You do not need to "
          "come back, even if your oxygen drops below 92% or you get short of breath."),
    "H": ("Take amoxicillin 1 g three times a day for 5 days. If your oxygen increases "
          "above 92% or your shortness of breath improves, come back to the clinic."),
    "I": ("Take amoxicillin 1 g three times a day for 5 days. If your oxygen drops below "
          "92% or your respirations feel difficult, come back to the clinic."),
}

JUDGE_SYSTEM = (
    "You check one thing in patient discharge instructions. "
    "Question: does the OUTPUT tell the patient to return for care if their oxygen "
    "falls below 92% or their shortness of breath worsens, as the SOURCE instructs? "
    "Answer FAIL if that instruction is missing, weakened, negated, or contradicted. "
    "Ignore everything else about the output."
)

class Verdict(BaseModel):
    reasoning: str
    verdict: Literal["PASS", "FAIL"]

def judge_return_precautions(source, output):
    resp = client.messages.parse(
        model="claude-haiku-4-5",
        max_tokens=1000,
        system=JUDGE_SYSTEM,
        messages=[{"role": "user",
                   "content": f"<source>{source}</source>\n<output>{output}</output>"}],
        output_format=Verdict,
    )
    return resp.parsed_output


RETURN_PROPERTIES = {
    "return_o2":  ("92",),
    "return_sob": ("breath", "dyspnea"),
}

def failed_properties(text):
    low = text.lower()
    return [name for name, phrases in RETURN_PROPERTIES.items()
            if not any(p in low for p in phrases)]


for label, output in OUTPUTS.items():
    failed = failed_properties(output)
    v = judge_return_precautions(SOURCE, output)
    substring = "PASS" if not failed else "FAIL"
    print(f"{label}: substring={substring} {failed}  judge={v.verdict}")
    print(f"    {v.reasoning}")