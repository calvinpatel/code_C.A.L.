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
    "I_er": ("Take amoxicillin 1 g three times a day for 5 days. If your oxygen drops below "
          "92% or your respirations feel difficult, come back to the ER."),
    "J": ("Take amoxicillin 1 g three times a day for 5 days. If your oxygen drops below "
          "92% or your respirations feel difficult, come back here to Dr. Grey."),
    "K": ("Take amoxicillin 1 g three times a day for 5 days. If your oxygen drops below "
          "92% or your respirations suddenly feel difficult, call 911."),
}

HUMAN_LABELS = {
    "A": "PASS",
    "G": "FAIL",   # negated
    "H": "FAIL",   # inverted
    "I": "FAIL",   # right triggers, wrong destination: clinic, not ED
    "I_er": "PASS", # right triggers, right destination: ER
    "J": "FAIL",    # named doctor, not the ED
    "K": "PASS",  # right triggers, right destination: 911
}

JUDGE_V1 = (
    "You check one thing in patient discharge instructions. "
    "Question: does the OUTPUT tell the patient to return for care if their oxygen "
    "falls below 92% or their shortness of breath worsens, as the SOURCE instructs? "
    "Answer FAIL if that instruction is missing, weakened, negated, or contradicted. "
    "Ignore everything else about the output."
)

JUDGE_V2 = (
    "You check one thing in patient discharge instructions. "
    "Question: does the OUTPUT tell the patient to go to the emergency department "
    "(ED or ER) if their oxygen falls below 92% or their shortness of breath worsens, "
    "as the SOURCE instructs? "
    "Answer FAIL if that instruction is missing, weakened, negated, or contradicted, "
    "or if it sends the patient anywhere other than the emergency department. "
    "Ignore everything else about the output."
)

class Verdict(BaseModel):
    reasoning: str
    verdict: Literal["PASS", "FAIL"]

def judge_return_precautions(source, output, system):
    resp = client.messages.parse(
        model="claude-haiku-4-5",
        max_tokens=1000,
        system=system,
        messages=[{"role": "user",
                   "content": f"<source>{source}</source>\n<output>{output}</output>"}],
        output_format=Verdict,
    )
    return resp.parsed_output

def grade_judge(system, outputs, labels):
    false_neg, false_pos = [], []
    for case_id, output in outputs.items():
        verdict = judge_return_precautions(SOURCE, output, system).verdict
        human = labels[case_id]
        if verdict == "PASS" and human == "FAIL":
            false_neg.append(case_id)
        elif verdict == "FAIL" and human == "PASS":
            false_pos.append(case_id)
        print(f"  {case_id}: judge={verdict}  human={human}")
    agree = len(outputs) - len(false_neg) - len(false_pos)
    print(f"  agreement {agree}/{len(outputs)}  false_neg={false_neg}  false_pos={false_pos}")

if __name__ == "__main__":
    for name, system in [("judge v1", JUDGE_V1), ("judge v2", JUDGE_V2)]:
        print(name)
        grade_judge(system, OUTPUTS, HUMAN_LABELS)