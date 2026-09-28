CASES = {
    "pna_amox": {
        "source": "Amoxicillin 1 g by mouth three times daily for 5 days. "
                  "Return to the ED if SpO2 < 92% or worsening shortness of breath.",
        "key": {
            "drug":      ("critical", ("amoxicillin",)),
            "frequency": ("critical", ("three times", "3 times")),
            "return_o2": ("critical", ("92",)),
            "duration":  ("warning",  ("5 days", "five days")),
        },
    },
    "uti_nitro": {
        "source": "Nitrofurantoin 100 mg by mouth twice daily for 5 days with food. "
                  "Return if fever or flank pain.",
        "key": {
            "drug":         ("critical", ("nitrofurantoin",)),
            "frequency":    ("critical", ("twice", "2 times", "two times")),
            "return_flank": ("critical", ("flank",)),
            "duration":     ("warning",  ("5 days", "five days")),
            "with_food":    ("info",     ("food",)),
        },
    },
    "strep_pen": {
        "source": "Penicillin V 500 mg by mouth twice daily for 10 days. "
                  "Return if fever or rash.",
        "key": {
            "drug":         ("critical", ("penicillin",)),
            "duration":     ("critical", ("10 days", "ten days")),
            "return_fever": ("critical", ("fever",)),
            "return_rash":  ("critical", ("rash", "hives")),
        },
    },
    "cellulitis_ceph": {
        "source": "Cephalexin 500 mg by mouth four times daily for 5 days. "
                  "Return if the redness spreads or you develop a fever.",
        "key": {
            "drug":          ("critical", ("cephalexin",)),
            "frequency":     ("critical", ("four times", "4 times")),
            "return_spread": ("critical", ("spread",)),
        },
    },
}

RUN_V1 = {   # prompt v1: the baseline
    "pna_amox": "Take amoxicillin 1 g three times a day for 5 days. "
                "Go to the ER if your oxygen drops below 92% or your breathing gets worse.",
    "uti_nitro": "Take nitrofurantoin 100 mg every day for 5 days with food. "
                 "Come back if you get flank pain or a fever.",
    "strep_pen": "Take penicillin 500 mg twice a day for 10 days. "
                 "Come back if you get a fever or a rash.",
    "cellulitis_ceph": "Take cephalexin 500 mg four times a day for 5 days. "
                       "Come back if you get a fever.",
}

RUN_V2 = {   # prompt v2: the candidate
    "pna_amox": "Take amoxicillin 1 g three times a day for 5 days. "
                "Go to the ER if your oxygen drops below 92% or your breathing gets worse.",
    "uti_nitro": "Take nitrofurantoin 100 mg twice a day for 5 days with food. "
                 "Come back if you get flank pain or a fever.",
    "strep_pen": "Take penicillin 500 mg twice a day for 10 days. "
                 "Come back if you get a rash.",
    "cellulitis_ceph": "Take cephalexin 500 mg four times a day for 5 days. "
                       "Come back if the redness spreads or you get a fever.",
}

RUN_V3 = {   # prompt v1 on a cheaper model: the candidate
    "pna_amox": "Take amoxicillin 1 g three times a day for 5 days. "
                "Go to the ER if your breathing gets worse.",
    "uti_nitro": "Take nitrofurantoin 100 mg twice a day with food. "
                 "Come back if you get flank pain or a fever.",
    "strep_pen": "Take penicillin 500 mg twice a day for 10 days. "
                 "Come back if you get a fever or a rash.",
    "cellulitis_ceph": "Take cephalexin 500 mg four times a day for 5 days. "
                       "Come back if you get a fever.",
}


def failed_properties(text, key):
    low = text.lower()
    return [(name, severity) for name, (severity, phrases) in key.items()
            if not any(p in low for p in phrases)]


def case_results(label, run):
    print(label)
    results = {}
    for case_id, output in run.items():
        failed = failed_properties(output, CASES[case_id]["key"])
        critical = [name for name, sev in failed if sev == "critical"]
        notes = [f"{name}({sev})" for name, sev in failed if sev != "critical"]
        results[case_id] = not critical
        print(f"  {case_id:16} {'FAIL' if critical else 'PASS'}  "
              f"critical={critical}  notes={notes}")
    return results


def pass_rate(results):
    passed = 0
    for ok in results.values():
        if ok:
            passed += 1
    return passed / len(results)


if __name__ == "__main__":
    base = case_results("baseline (prompt v1):", RUN_V1)
    new = case_results("candidate (prompt v2):", RUN_V2)
    base_rate, new_rate = pass_rate(base), pass_rate(new)
    print(f"pass rate {base_rate:.2f} -> {new_rate:.2f}")
    if new_rate >= base_rate:
        print("gate: no regression, ship it")
    else:
        print("gate: REGRESSION")