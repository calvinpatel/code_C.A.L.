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
    "strep_pen": {
        "source": ("Discharge: penicillin V 500 mg by mouth twice daily for 10 days. "
                   "Finish the full course even if you feel better. Return if you develop a fever or a rash."),
        "key": {
            "drug":         ("critical", ("penicillin", "penicillin V")),
            "dose":         ("critical", (" 500 mg",)),
            "frequency":    ("critical", ("twice", "2 times", "two times")),
            "duration":     ("critical",  ("10 days", "ten days", "full course")),
            "return_fever": ("critical", ("fever",)),
            "return_rash":  ("critical", ("rash", "hives")),
        },
    },
}

RUN_V1 = {
    "pna_amox":  ("Take amoxicillin 1 g three times a day for 5 days. Come back if your "
                  "oxygen is below 92% or you get more short of breath."),
    "uti_nitro": ("Take nitrofurantoin 100 mg twice a day. Return if you get a fever "
                  "or flank pain."),
    "strep_pen": ("Take penicillin 500 mg twice a day for 10 days, and finish all of it. "
                  "Come back if you get a rash."),
}

RUN_V2 = {
    "pna_amox":  ("Take amoxicillin 1 g three times a day for 5 days, with food if your "
                  "stomach is upset. Come back if you feel more short of breath."),
    "uti_nitro": ("Take nitrofurantoin 100 mg twice a day for 5 days with food. Return "
                  "if you get a fever or flank pain."),
    "strep_pen": ("Take penicillin 500 mg twice a day until you feel better. "
                  "Come back if you get a fever or a rash."),
}

def failed_properties(text, key):
    low = text.lower()
    return [(name, severity) for name, (severity, phrases) in key.items()
            if not any(p in low for p in phrases)]


def flat_score(run):
    passed = 0
    for case_id, output in run.items():
        failed = failed_properties(output, CASES[case_id]["key"])
        names = [name for name, sev in failed]
        if not failed:
            passed += 1
        print(f"  {case_id:10} {'FAIL' if failed else 'PASS'}  {names}")
    return passed / len(run)


def gated_score(run):
    passed = 0
    for case_id, output in run.items():
        failed = failed_properties(output, CASES[case_id]["key"])
        critical = [name for name, sev in failed if sev == "critical"]
        notes = [f"{name}({sev})" for name, sev in failed if sev != "critical"]
        if not critical:
            passed += 1
        print(f"  {case_id:10} {'FAIL' if critical else 'PASS'}  "
              f"critical={critical}  notes={notes}")
    return passed / len(run)


def validate_keys(cases):
    for case_id, case in cases.items():
        if not any(sev == "critical" for sev, phrases in case["key"].values()):
            raise ValueError(f"{case_id}: key has no critical property")


validate_keys(CASES)


for scorer in [flat_score, gated_score]:
    print(f"=== {scorer.__name__} ===")
    for label, run in [("prompt v1", RUN_V1), ("prompt v2", RUN_V2)]:
        print(f"{label}:")
        rate = scorer(run)
        print(f"  pass rate = {rate:.2f}")