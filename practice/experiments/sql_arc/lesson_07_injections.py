import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("""
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    name       TEXT,
    birth_year INTEGER,
    site       TEXT
)
""")
cur.executemany("INSERT INTO patients VALUES (?, ?, ?, ?)", [
    (1, "Ava Chen",    1991, "Baltimore"),
    (2, "Marcus Reid", 1978, "Bethesda"),
    (3, "Lena Okafor", 2002, "Baltimore"),
    (4, "Ava Chen",    1995, "Bethesda"),   # a second "Ava Chen" — handy for testing
])
conn.commit()


# ── PART 1: rewrite this safely (kill the f-string) ──────────────
def find_by_name(cur, name):
    return cur.execute("SELECT * FROM patients WHERE name = ?", (name,)).fetchall()


# ── PART 2: make sort_col safe too (placeholder won't work here — why?) ──
ALLOWED_SORT = ["name", "birth_year", "site"]

def find_by_name_sorted(cur, name, sort_col):
    if sort_col not in ALLOWED_SORT:
        raise ValueError(f"invalid sort_col: {sort_col!r}")
    # sort_col is now guaranteed to be one of 3 strings I chose — safe to interpolate
    return cur.execute(
        f"SELECT * FROM patients WHERE name = ? ORDER BY {sort_col}",
        (name,),
    ).fetchall()


# ── test harness ──────────────────────────────────────────────
print("Part 1 — normal:", find_by_name(cur, "Ava Chen"))
print("Part 1 — attack:", find_by_name(cur, "' OR '1'='1"))   # should return [] once fixed

print("Part 2 — sorted:", find_by_name_sorted(cur, "Ava Chen", "birth_year"))
print("Part 2 — attack:", find_by_name_sorted(cur, "Ava Chen", "birth_year; DROP TABLE patients"))