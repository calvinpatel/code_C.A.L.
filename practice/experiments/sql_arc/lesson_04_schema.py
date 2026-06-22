import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("PRAGMA foreign_keys = ON")
cur = conn.cursor()

#create tables (DDL)
cur.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        patient_birth_year INTEGER CHECK (patient_birth_year >= 1900)
)
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS drugs (
        drug_id INTEGER PRIMARY KEY,
        drug_class TEXT NOT NULL,
        name TEXT NOT NULL
)
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS prescriptions (
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

#Create indexes (DDL)
cur.execute("""
    CREATE INDEX IF NOT EXISTS idx_prescriptions_patient_id ON prescriptions(patient_id)
""")

cur.execute("""
    CREATE INDEX IF NOT EXISTS idx_prescriptions_drug_id ON prescriptions(drug_id)
""")

cur.execute("""
    CREATE INDEX IF NOT EXISTS idx_patients_name ON patients(name)
""")

conn.commit()
conn.close()