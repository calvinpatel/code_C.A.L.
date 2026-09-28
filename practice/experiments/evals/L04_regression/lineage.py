import json
import sys
from datetime import datetime
from pathlib import Path

from harness import RUN_V1, RUN_V2, RUN_V3, case_results, pass_rate

HISTORY = Path("corpus_runs.jsonl")
CORPUS_VERSION = "c1"


def record_run(run, model, prompt_version):
    results = case_results(f"{model} / prompt {prompt_version}:", run)
    record = {
        "ran_at": datetime.now().isoformat(),
        "model": model,
        "prompt_version": prompt_version,
        "corpus_version": CORPUS_VERSION,
        "pass_rate": pass_rate(results),
        "results": results,
    }
    with open(HISTORY, "a") as f:
        f.write(json.dumps(record) + "\n")
    return results


def load_history():
    with open(HISTORY) as f:
        return [json.loads(line) for line in f]


def find_baseline(history, model, prompt_version):
    matches = [r for r in history
               if r["model"] == model and r["prompt_version"] == prompt_version]
    if not matches:
        raise ValueError(
            f"No baseline found for model {model!r} and prompt version {prompt_version!r}"
        )
    return matches[-1]["results"]


def diff_runs(base, new):
    base_pass = {case_id for case_id, ok in base.items() if ok}
    new_pass = {case_id for case_id, ok in new.items() if ok}
    regressions = base_pass - new_pass
    fixes = new_pass - base_pass
    still_failing = set(base.keys()) - (base_pass | new_pass)
    return regressions, fixes, still_failing


record_run(RUN_V1, "model-large", "v1")           # production config
new = record_run(RUN_V3, "model-small", "v1")     # the candidate

history = load_history()
print(f"history: {len(history)} runs on file")
for r in history:
    print(f"  {r['ran_at'][:19]}  {r['model']:12} prompt {r['prompt_version']}  "
          f"rate {r['pass_rate']:.2f}")

base = find_baseline(history, "model-large", "V1")
regressions, fixes, still_failing = diff_runs(base, new)
print(f"regressions   = {sorted(regressions)}")
print(f"fixes         = {sorted(fixes)}")
print(f"still_failing = {sorted(still_failing)}")
if regressions:
    print("gate: REGRESSION")
    sys.exit(1)
print("gate: no regression")