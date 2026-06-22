import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")

cur.execute("""
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    patient_birth_year INTEGER CHECK (patient_birth_year >= 1900)
)
""")

cur.execute("""
CREATE TABLE drugs (
    drug_id INTEGER PRIMARY KEY,
    drug_class TEXT NOT NULL,
    name TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE prescriptions (
    rx_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    drug_id INTEGER NOT NULL,
    dose_amount REAL NOT NULL CHECK (dose_amount > 0),
    dose_unit TEXT NOT NULL CHECK (dose_unit IN ('mg', 'ml', 'mcg', 'g')),
    prescribed_date TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (drug_id) REFERENCES drugs(drug_id)
)
""")