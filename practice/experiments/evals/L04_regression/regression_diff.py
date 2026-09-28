from harness import RUN_V1, RUN_V2, RUN_V3, case_results, pass_rate


def diff_runs(base, new):
    base_pass = {case_id for case_id, ok in base.items() if ok}
    new_pass = {case_id for case_id, ok in new.items() if ok}
    regressions = base_pass - new_pass
    fixes = new_pass - base_pass
    still_failing = set(base.keys()) - (base_pass | new_pass)
    return regressions, fixes, still_failing


base = case_results("baseline (prompt v1):", RUN_V1)
new = case_results("candidate (prompt v1 cheap):", RUN_V3)
regressions, fixes, still_failing = diff_runs(base, new)

print(f"pass rate {pass_rate(base):.2f} -> {pass_rate(new):.2f}")
print(f"regressions = {sorted(regressions)}")
print(f"fixes       = {sorted(fixes)}")
print(f"still failing = {sorted(still_failing)}")
print("gate:", "REGRESSION" if regressions else "no regression")