import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    birth_year INTEGER,
    allergy    TEXT,
    site       TEXT
)
""")
cur.executemany(
    "INSERT INTO patients VALUES (?, ?, ?, ?, ?)",
    [
        (1, "Ava Chen",    1991, "penicillin", "Baltimore"),
        (2, "Marcus Reid", 1978, None,         "Baltimore"),
        (3, "Lena Okafor", 2002, "sulfa",      "Bethesda"),
        (4, "Sam Park",    1995, "penicillin", "Baltimore"),
        (5, "Tariq Bell",  1988, None,         "Bethesda"),
        (6, "Nora Diaz",   2000, "sulfa",      "Baltimore"),
    ],
)
conn.commit()

def run(label, sql):
    print(f"--- {label} ---")
    for row in cur.execute(sql):
        print(row)
    print()

run("ORDER BY",     "SELECT name, birth_year FROM patients ORDER BY birth_year")
run("LIMIT",        "SELECT name, birth_year FROM patients ORDER BY birth_year DESC LIMIT 3")
run("DISTINCT",     "SELECT DISTINCT site FROM patients")
run("aggregates",   "SELECT COUNT(*), COUNT(allergy), AVG(birth_year) FROM patients")
run("GROUP BY",     "SELECT site, COUNT(*) AS n FROM patients GROUP BY site ORDER BY n DESC")
run("HAVING",       "SELECT site, COUNT(*) AS n FROM patients GROUP BY site HAVING COUNT(*) > 2")

# your challenge query goes here ↓
run("ALLERGIES", "SELECT allergy, COUNT(*) AS n FROM patients WHERE allergy IS NOT NULL GROUP BY allergy ORDER BY n DESC")
run("ALLERGIES", "SELECT allergy, COUNT(*) AS n FROM patients GROUP BY allergy HAVING allergy IS NOT NULL ORDER BY n DESC")
