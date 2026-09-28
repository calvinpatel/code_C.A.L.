# The answer key: one entry per case, written once by someone with clinical authority.
CASES = {
    "pna_amox": {
        "source": ("Dx: community-acquired pneumonia. Rx amoxicillin 1 g PO TID x 5 days. "
                   "Return if SpO2 < 92% or worsening dyspnea."),
        "key": {
            "drug":       ("amoxicillin",),
            "dose":       ("1 g", "1 gram", "1000 mg"),
            "frequency":  ("three times", "3 times", "every 8 hours"),
            "duration":   ("5 days", "five days"),
            "return_o2":  ("92",),
            "return_sob": ("breath", "dyspnea"),
        },
    },
    "uti_nitro": {
        "source": ("Dx: uncomplicated cystitis. Rx nitrofurantoin 100 mg PO BID x 5 days. "
                   "Return if fever or flank pain."),
        "key": {
            "drug":         ("nitrofurantoin",),
            "dose":         ("100 mg",),
            "frequency":    ("twice", "two times", "2 times", "every 12 hours"),
            "duration":     ("5 days", "five days"),
            "return_fever": ("fever",),
            "return_flank": ("flank", "side"),
        },
    },
    "strep_penicillin": {
        "source": ("Dx: strep pharyngitis. Rx penicillin V 500 mg PO BID x 10 days. "
                   "Return if fever or rash."),
        "key": {
            "drug":         ("penicillin", "penicillin v"),
            "dose":         (" 500 mg",),
            "frequency":    ("twice", "two times", "2 times", "every 12 hours"),
            "duration":     ("10 days", "ten days"),
            "return_fever": ("fever",),
            "return_rash":  ("rash", "hives",),
        },
    },
}

# Two runs: one model output per case. Hand-written stand-ins, not model calls.
RUN_V1 = {
    "pna_amox":  ("Your lung infection (pneumonia) is treated with amoxicillin, 1 gram, 3 times "
                  "daily for five days. Return to the ER if breathing worsens or oxygen is under 92%."),
    "uti_nitro": ("You have a bladder infection. Take nitrofurantoin 100 mg once a day for "
                  "5 days. Come back if you get a fever or pain in your side."),
    "strep_penicillin": ("You have strep throat. Take penicillin V 500 mg twice a day for 10 days. "
                         "Come back if you develop a fever or an unexplained rash.")
}
RUN_V2 = {
    "pna_amox":  ("Pneumonia: take 1000 mg of amoxicillin three times daily for 5 days. Come back "
                  "if you get more short of breath or your oxygen reads below 92%."),
    "uti_nitro": ("Bladder infection: take nitrofurantoin 100 mg two times a day for five days. "
                  "Return for fever or flank pain."),
    "strep_penicillin": ("Strep throat: take penicillin 500 mg every 12 hours for ten days. "
                         "Return if you develop high temperature or a rash.")
}

def failed_properties(text, key):
    low = text.lower()
    return [name for name, phrases in key.items()
            if not any(p in low for p in phrases)]

def score(run):
    passed = 0
    for case_id, output in run.items():
        failed = failed_properties(output, CASES[case_id]["key"])
        if not failed:
            passed += 1
        print(f"  {case_id:10} {'PASS' if not failed else 'FAIL'}  {failed}")
    return passed / len(run)

if __name__ == "__main__":
    for name, run in [("v1", RUN_V1), ("v2", RUN_V2)]:
        print(f"prompt {name}:")
        print(f"  pass rate = {score(run):.2f}")