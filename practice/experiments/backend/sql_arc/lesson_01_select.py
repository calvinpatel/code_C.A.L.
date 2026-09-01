import sqlite3

conn = sqlite3.connect("clinic.db")   # ":memory:" = ephemeral DB, gone when script ends
cur = conn.cursor()                  # a cursor is your "hand" that runs SQL + holds results

# DDL = Data Definition Language → defines the SHAPE of data
cur.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id   INTEGER PRIMARY KEY,
    name         TEXT NOT NULL,
    birth_year   INTEGER,
    allergy      TEXT
)
""")

# DML = Data Manipulation Language → moves data IN and OUT
cur.executemany(
    "INSERT OR IGNORE INTO patients (patient_id, name, birth_year, allergy) VALUES (?, ?, ?, ?)",
    [                                  # the ? are placeholders — NEVER f-string user data into SQL
        (1, "Ava Chen",    1991, "penicillin"),
        (2, "Marcus Reid", 1978, None),          # None becomes NULL in the DB
        (3, "Lena Okafor", 2002, "sulfa"),
    ]
)
conn.commit()                          # commit = actually save the changes

print("--- Q1: everything ---")
for row in cur.execute("SELECT * FROM patients"):
    print(row)

print("--- Q2: just two columns ---")
for row in cur.execute("SELECT name, allergy FROM patients"):
    print(row)

print("--- Q3: only patients WITH an allergy ---")
for row in cur.execute("SELECT name, allergy FROM patients WHERE allergy IS NOT NULL"):
    print(row)

print("--- Q4: Only patients born AFTER 1985 ---")
for row in cur.execute("SELECT name FROM patients WHERE birth_year > 1985"):
    print(row)