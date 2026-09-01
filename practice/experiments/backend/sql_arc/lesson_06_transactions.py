import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("PRAGMA foreign_keys = ON")          # FK enforcement live — matters for this challenge
cur = conn.cursor()

# --- schema ---
cur.execute("CREATE TABLE patients (patient_id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
cur.execute("""
CREATE TABLE prescriptions (
    rx_id      INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    drug_name  TEXT    NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
)
""")

# --- seed: same person entered twice (id 2 AND id 7), prescriptions split across both ---
cur.executemany("INSERT INTO patients VALUES (?, ?)",
                [(2, "Ava Chen"), (7, "Ava Chen")])
cur.executemany("INSERT INTO prescriptions VALUES (?, ?, ?)", [
    (101, 2, "amoxicillin"),
    (102, 7, "ibuprofen"),      # belongs to the duplicate (#7)
    (103, 7, "lisinopril"),     # belongs to the duplicate (#7)
])
conn.commit()

def snapshot(label):
    print(f"--- {label} ---")
    print("  patients:     ", cur.execute("SELECT patient_id, name FROM patients ORDER BY patient_id").fetchall())
    print("  prescriptions:", cur.execute("SELECT rx_id, patient_id FROM prescriptions ORDER BY rx_id").fetchall())

snapshot("BEFORE merge")

# ┌─────────────────────────────────────────────────────────────┐
# │  YOUR CHALLENGE: merge patient #7 into #2 as ONE transaction │
# │  - reassign #7's prescriptions onto #2  (one UPDATE)          │
# │  - delete patient #7                    (one DELETE)          │
# │  - wrap both in a `with conn:` block                         │
# │  - mind the ORDER (FK enforcement is ON)                     │
# └─────────────────────────────────────────────────────────────┘

with conn:
    cur.execute("UPDATE prescriptions SET patient_id = 2 WHERE patient_id = 7")
    cur.execute("DELETE FROM patients WHERE patient_id = 7")

snapshot("AFTER merge")   # expect: only patient 2 remains; all 3 prescriptions point to 2