from grade_judge import SOURCE, OUTPUTS, JUDGE_V2, judge_return_precautions

verdicts = []
for run in range(10):
    v = judge_return_precautions(SOURCE, OUTPUTS["K"], JUDGE_V2)
    verdicts.append(v.verdict)
    print(f"run {run}: {v.verdict}  | {v.reasoning[:90]}")

print(f"PASS {verdicts.count('PASS')}/10  FAIL {verdicts.count('FAIL')}/10")