# safety.py
PENICILLIN_CLASS = {"amoxicillin", "ampicillin", "augmentin", "penicillin"}
#   ↑ amoxicillin/ampicillin/augmentin are all penicillin-class drugs.
#     a patient allergic to penicillin is contraindicated for ALL of them.

def find_allergy_conflicts(prescribed: list[str], allergies: list[str]) -> list[str]:
    """Return the prescribed drugs that conflict with a known allergy.
    Errors-as-values: returns a list of conflicts, never raises."""
    allergic_to_penicillin = any(drug in PENICILLIN_CLASS for drug in allergies)

    if not allergic_to_penicillin:
        return []

    conflicts = []
    for drug in prescribed:
        if drug in PENICILLIN_CLASS:
            conflicts.append(drug)
    return conflicts