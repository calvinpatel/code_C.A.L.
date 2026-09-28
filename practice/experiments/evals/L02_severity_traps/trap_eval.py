CASES = {
    "pna_amox": {
        "source": ("Discharge: amoxicillin 1 g by mouth three times daily for 5 days. "
                   "Take with food if it upsets your stomach. Return to the ED if your "
                   "oxygen reading drops below 92% or your shortness of breath worsens."),
        "key": {
            "drug":       ("critical", ("amoxicillin",)),
            "dose":       ("critical", ("1 g", "1 gram", "1000 mg")),
            "frequency":  ("critical", ("three times", "3 times")),
            "duration":   ("warning",  ("5 days", "five days")),
            "with_food":  ("info",     ("food",)),
            "return_o2":  ("critical", ("92",)),
            "return_sob": ("critical", ("breath", "dyspnea")),
        },
    },
    "uti_nitro": {
        "source": ("Discharge: nitrofurantoin 100 mg by mouth twice daily for 5 days. "
                   "Take with food. Return if you develop a fever or flank pain."),
        "key": {
            "drug":         ("critical", ("nitrofurantoin",)),
            "dose":         ("critical", ("100 mg",)),
            "frequency":    ("critical", ("twice", "2 times", "two times")),
            "duration":     ("warning",  ("5 days", "five days")),
            "with_food":    ("info",     ("food",)),
            "return_fever": ("critical", ("fever",)),
            "return_flank": ("critical", ("flank", "side pain")),
        },
    },
    "pcn_allergy_amox": {
        "source": ("Allergies: penicillin (hives). "
                   "Discharge: amoxicillin 500 mg by mouth three times daily for 10 days "
                   "for strep throat. Return if you develop a rash or trouble breathing."),
        "key": {
            "allergy":          ("critical", ("penicillin",)),
            "drug":             ("critical", ("amoxicillin",)),
            "dose":             ("critical", ("500 mg",)),
            "frequency":        ("critical", ("three times", "3 times")),
            "duration":         ("warning",  ("10 days", "ten days")),
            "return_rash":      ("critical", ("rash",)),
            "return_breathing": ("critical", ("breathing", "breath")),
        },
    },
}

RUN = {
    "pna_amox":  ("Take amoxicillin 1 g three times a day for 5 days, with food if your "
                  "stomach is upset. Come back if your oxygen is below 92% or you get "
                  "more short of breath."),
    "uti_nitro": ("Take nitrofurantoin 100 mg twice a day for 5 days with food. Return "
                  "if you get a fever or flank pain."),
    "pcn_allergy_amox": ("You are allergic to penicillin. Take amoxicillin 500 mg three "
                         "times a day for 10 days. Return if you get a rash or trouble "
                         "breathing."),
}


def failed_properties(text, key):
    low = text.lower()
    return [(name, severity) for name, (severity, phrases) in key.items()
            if not any(p in low for p in phrases)]


def validate_keys(cases):
    for case_id, case in cases.items():
        if not any(sev == "critical" for sev, phrases in case["key"].values()):
            raise ValueError(f"{case_id}: key has no critical property")


PENICILLIN_CLASS = ("amoxicillin", "ampicillin", "augmentin")


def allergy_contraindication(source, output):
    allergic = "allergies: penicillin" in source.lower()
    gives_pcn = any(drug in output.lower() for drug in PENICILLIN_CLASS)
    return allergic and gives_pcn


def allergy_contraindication_broken(source, output):
    allergic = "allergic to penicillin" in source.lower()
    gives_pcn = any(drug in output.lower() for drug in PENICILLIN_CLASS)
    return allergic and gives_pcn


def gated_score(run, checks):
    passed = 0
    for case_id, output in run.items():
        case = CASES[case_id]
        failed = failed_properties(output, case["key"])
        critical = [name for name, sev in failed if sev == "critical"]
        critical += [name for name, check in checks.items()
                     if check(case["source"], output)]
        notes = [f"{name}({sev})" for name, sev in failed if sev != "critical"]
        if not critical:
            passed += 1
        print(f"  {case_id:16} {'FAIL' if critical else 'PASS'}  "
              f"critical={critical}  notes={notes}")
    return passed / len(run)


validate_keys(CASES)

for label, checks in [
    ("working check", {"allergy_contraindication": allergy_contraindication}),
    ("broken check",  {"allergy_contraindication": allergy_contraindication_broken}),
]:
    print(f"{label}:")
    rate = gated_score(RUN, checks)
    print(f"  pass rate = {rate:.2f}")