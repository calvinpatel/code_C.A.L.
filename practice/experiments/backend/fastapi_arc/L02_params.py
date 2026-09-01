from dataclasses import dataclass
from fastapi import FastAPI

app = FastAPI()

@dataclass
class Prescription:
    name: str
    is_active: bool

# hardcoded stand-in for "the database" — patient 7 has 5 scripts, 2 discontinued
_DB = {
    7: [
        Prescription("amoxicillin", True),
        Prescription("lisinopril", True),
        Prescription("old_antibiotic", False),
        Prescription("metformin", True),
        Prescription("discontinued_nsaid", False),
    ]
}

def get_prescriptions(patient_id: int) -> list[Prescription]:
    return _DB.get(patient_id, [])              # [] if the patient isn't found

@app.get("/patients/{patient_id}/prescriptions")
def list_rx(patient_id: int, active: bool = True, limit: int = 20):
    rx = get_prescriptions(patient_id)          # 1. fetch all
    if active:                                  # 2. maybe filter to active
        rx = [r for r in rx if r.is_active]
    return rx[:limit]                           # 3. cap to limit