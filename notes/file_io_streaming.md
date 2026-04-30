# 📝 The Streaming File Pattern — Cheat Sheet

> *Pulled from the File I/O arc with Claudia. Reference whenever processing files larger than RAM, or whenever defensive parsing is needed.*

---

## The mental trigger 🧠

**Ask yourself FIRST:** *"Could this file be bigger than my RAM?"*

- **Yes** → use the streaming pattern below
- **No, but I want defensive parsing anyway** → still use this. It's the right pattern for any non-trivial file work.

---

## The skeleton (memorize this shape)

```python
import csv
from pathlib import Path

input_path = Path("input.csv")
output_path = Path("output.csv")

match_count = 0
error_count = 0

with open(input_path, "r", encoding="utf-8", errors="replace") as fin, \
     open(output_path, "w", encoding="utf-8", newline="") as fout:

    reader = csv.DictReader(fin)
    writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
    writer.writeheader()

    for line_num, row in enumerate(reader, start=2):
        try:
            if row["mutation_type"] == "frameshift":  # <-- your filter
                writer.writerow(row)
                match_count += 1
        except (KeyError, ValueError):
            error_count += 1
            continue

print(f"✅ Matched: {match_count}")
print(f"⚠️  Errors:  {error_count}")
```

That's the pattern. Six moving parts. Break each down below. 👇

---

## Anatomy of the pattern

### 1️⃣ The double `with` (open BOTH files in one statement)

```python
with open(input_path, "r", ...) as fin, \
     open(output_path, "w", ...) as fout:
```

**Why:** opens both files as context managers. **Both get auto-closed** even if something crashes mid-loop. The `\` is just line continuation for readability — it's all one `with` statement.

**Mental shortcut:** `fin` = "file in", `fout` = "file out". Cute. Sticks. 💅🏻

---

### 2️⃣ The argument cocktail for `open()`

```python
"r", encoding="utf-8", errors="replace"     # for reading
"w", encoding="utf-8", newline=""            # for writing CSV
```

**Read side cheat:**

| Argument | Purpose |
|---|---|
| `"r"` | Read mode |
| `encoding="utf-8"` | Don't trust OS defaults |
| `errors="replace"` | Survive bad bytes — corrupt chars become `�` |

**Write side cheat:**

| Argument | Purpose |
|---|---|
| `"w"` | Write mode (wipes existing file) |
| `encoding="utf-8"` | Don't trust OS defaults |
| `newline=""` | **CSV-specific** — prevents phantom blank rows on Windows |

🚨 **Memorize:** `newline=""` belongs to **writing CSVs**, not reading. Reading doesn't need it.

---

### 3️⃣ DictReader → DictWriter schema handoff

```python
reader = csv.DictReader(fin)
writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
writer.writeheader()
```

**The clever move:** `reader.fieldnames` is the list of column names DictReader pulled from the input header. You hand it directly to DictWriter so the output file has the **same column structure as the input**. No hand-typing column names. No drift between input and output schemas.

Then `writer.writeheader()` writes the header row to the output file so it's also a valid CSV.

```
INPUT HEADER          →    DictReader.fieldnames    →    DictWriter writes
patient_id,           →    ['patient_id',           →    patient_id,
mutation_type,             'mutation_type',              mutation_type,
chromosome                 'chromosome']                 chromosome
```

---

### 4️⃣ `enumerate(reader, start=2)`

```python
for line_num, row in enumerate(reader, start=2):
```

**Why `start=2`?** Line 1 of the file was the header (DictReader already consumed it). The first *data* row is line 2. So `line_num` matches what you'd see if you opened the file in a text editor — useful for error reports.

```
File line 1:  patient_id,mutation_type,...     ← header (consumed by DictReader)
File line 2:  P001,frameshift,chr7              ← line_num=2 ✅
File line 3:  P002,missense,chr3                ← line_num=3 ✅
```

---

### 5️⃣ The defensive `try/except`

```python
try:
    if row["mutation_type"] == "frameshift":
        writer.writerow(row)
        match_count += 1
except (KeyError, ValueError):
    error_count += 1
    continue
```

**What can go wrong per row:**

| Exception | When it fires |
|---|---|
| `KeyError` | Column name missing (header was malformed) |
| `ValueError` | Type conversion failed (e.g., `int("abc")`) |
| `IndexError` | Positional access went out of bounds |

**Catch ONLY what you expect.** Don't `except Exception:` — that swallows real bugs. Catch the specific exceptions that mean "bad row, skip it."

`continue` = "skip this row, move on to the next one." The loop survives.

---

### 6️⃣ Counters (not lists!) for big-file work

```python
match_count = 0          # ← integer counter, NOT a list
error_count = 0
```

**The trap:** if you write `matches = []` and `.append()` every match, then on a 2 GB file with 500K matches, `matches` itself becomes huge. **Counters use constant memory regardless of file size.**

**Rule:** for streaming work, write matches to a file as you find them. Use counters in memory for stats. Never accumulate big lists.

---

## The memory diagram (this is the whole point)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   2 GB INPUT FILE                       OUTPUT FILE         │
│   ───────────────                       ───────────         │
│                                                             │
│   row 1   ───►  ┌─────────────┐  ───►   (filtered out)      │
│   row 2   ───►  │             │  ───►   row 2 (match!)      │
│   row 3   ───►  │   1 ROW     │  ───►   (filtered out)      │
│   row 4   ───►  │   IN RAM    │  ───►   row 4 (match!)      │
│   ...           │             │         ...                 │
│   row 50M ───►  └─────────────┘  ───►   (filtered out)      │
│                                                             │
│   ▲                  ▲                       ▲              │
│   never loaded   constant memory      matches written       │
│   in full        (one row)            as found              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**KEY INSIGHT:** RAM usage is FLAT regardless of input size. 1 GB file? Same RAM. 1 TB file? Same RAM.

This is the magic. Streaming means you process arbitrarily large data with bounded memory.

---

## Variations on the theme 🎨

### Variation A: Just count, don't write

```python
with open(input_path, "r", encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    count = sum(1 for row in reader if row.get("mutation_type") == "frameshift")
print(f"Total frameshift mutations: {count}")
```

The generator expression `1 for row in reader if ...` is fully streaming. `sum()` consumes it one item at a time. Beautiful.

### Variation B: Write to JSON instead of CSV

```python
import json

with open(input_path, "r", encoding="utf-8") as fin, \
     open("matches.jsonl", "w", encoding="utf-8") as fout:

    reader = csv.DictReader(fin)
    for row in reader:
        if row["mutation_type"] == "frameshift":
            fout.write(json.dumps(row) + "\n")
```

⚠️ **Note:** this writes **JSON Lines** (`.jsonl`) — one JSON object per line — NOT a single JSON array. This is the standard format for streaming JSON in big-data work. Loading the whole thing as one giant JSON array would defeat the streaming pattern.

### Variation C: Multiple filters at once

```python
match_counts = {"frameshift": 0, "missense": 0, "nonsense": 0}

with open(input_path, "r", encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for row in reader:
        mtype = row.get("mutation_type")
        if mtype in match_counts:
            match_counts[mtype] += 1

print(match_counts)
```

One pass through the file, multiple filters tracked simultaneously. **Always prefer one streaming pass with multiple counters over multiple passes through the same file.**

---

## The "danger zone" — when streaming patterns leak ⚠️

Even with streaming, you can accidentally blow up memory. Watch for:

```python
# 🚨 BAD — accumulates everything
matches = [row for row in reader if row["mutation_type"] == "frameshift"]

# 🚨 BAD — sorting requires loading everything
sorted_rows = sorted(reader, key=lambda r: r["chromosome"])

# 🚨 BAD — pandas defaults to loading everything
import pandas as pd
df = pd.read_csv("huge.csv")   # loads 2 GB into RAM

# ✅ GOOD — pandas in chunks
for chunk in pd.read_csv("huge.csv", chunksize=10_000):
    process(chunk)
```

**Sorting and grouping fundamentally need the whole dataset.** If you absolutely must sort a file that doesn't fit in RAM, that's "external sort" territory — Phase 4 problem. For now: stick to filtering, counting, and transforming row-by-row.

---

## The 30-second mental checklist 🎯

When you see a file processing task, run through this in your head:

1. ☐ Is the file big enough to worry about RAM?
2. ☐ Am I using `with` (or double `with`) for cleanup?
3. ☐ Did I specify `encoding="utf-8"` explicitly?
4. ☐ If writing CSV, did I add `newline=""`?
5. ☐ Am I using DictReader/DictWriter for named access?
6. ☐ Is my parsing wrapped in try/except?
7. ☐ Do I track errors with line numbers?
8. ☐ Am I using counters instead of accumulating big lists?
9. ☐ If I'm writing matches, am I writing AS I FIND THEM (not after)?

If you can check all 9, the code is production-shaped. ⚔️

---

## The vibe summary 💅🏻

> The streaming pattern is just the same pattern you've already been writing — `for line in f`, `try`, `except`, `continue` — with two upgrades:
>
> 1. Use the `csv` module (DictReader/DictWriter) instead of `split()`
> 2. Write outputs as you go, not after
>
> That's it. You already know everything else.

---

*From the File I/O arc — Cal × Claudia, April 2026* ⚔️
