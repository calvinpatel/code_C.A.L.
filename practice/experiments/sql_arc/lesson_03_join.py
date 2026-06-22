import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL
)
""")
cur.execute("""
CREATE TABLE visits (
    visit_id   INTEGER PRIMARY KEY,
    patient_id INTEGER,
    visit_date TEXT,
    reason     TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
)
""")
cur.executemany("INSERT INTO patients VALUES (?, ?)",
                [(1, "Ava Chen"), (2, "Marcus Reid"), (3, "Lena Okafor")])
cur.executemany("INSERT INTO visits VALUES (?, ?, ?, ?)", [
    (501, 1, "2026-03-02", "follow-up"),
    (502, 1, "2026-05-14", "labs"),
    (503, 2, "2026-04-09", "intake"),
])  # Lena (3) deliberately has no visits
conn.commit()

def run(label, sql):
    print(f"--- {label} ---")
    for row in cur.execute(sql):
        print(row)
    print()

run("INNER JOIN",
    """SELECT p.name, v.visit_date, v.reason
       FROM patients p
       JOIN visits v ON p.patient_id = v.patient_id""")

run("LEFT JOIN",
    """SELECT p.name, v.visit_date, v.reason
       FROM patients p
       LEFT JOIN visits v ON p.patient_id = v.patient_id""")

run("visits per patient (note COUNT(v.visit_id), not COUNT(*))",
    """SELECT p.name, COUNT(v.visit_id) AS visits
       FROM patients p
       LEFT JOIN visits v ON p.patient_id = v.patient_id
       GROUP BY p.patient_id
       ORDER BY visits DESC""")

run("anti-join: patients who never visited",
    """SELECT p.name
       FROM patients p
       LEFT JOIN visits v ON p.patient_id = v.patient_id
       WHERE v.visit_id IS NULL""")

# CHALLENGE: every patient + their most recent visit date (NULL if none), ordered by name.
# your query here ↓
run("patient + most recent visit date",
    """SELECT p.name, MAX(v.visit_date) AS most_recent_visit
    FROM patients p
    LEFT JOIN visits v ON p.patient_id = v.patient_id
    GROUP BY p.patient_id
    ORDER BY p.name""")