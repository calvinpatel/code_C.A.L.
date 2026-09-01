from sqlalchemy import create_engine, text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session


class Base(DeclarativeBase): pass

class Patient(Base):
    __tablename__ = "patients"
    patient_id: Mapped[int] = mapped_column(primary_key=True)
    name:       Mapped[str] = mapped_column()
    birth_year: Mapped[int | None] = mapped_column()
    prescriptions: Mapped[list["Prescription"]] = relationship(back_populates="patient")

class Prescription(Base):
    __tablename__ = "prescriptions"
    rx_id:      Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.patient_id"))
    drug_name:  Mapped[str] = mapped_column()
    patient:    Mapped["Patient"] = relationship(back_populates="prescriptions")


engine = create_engine("sqlite:///:memory:")   # disposable practice DB
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([
        Patient(name="Ava Chen", birth_year=1991, prescriptions=[
            Prescription(drug_name = "amoxicillin"),
            Prescription(drug_name = "vancomycin"),
        ]),
        Patient(name="Marcus Reid", birth_year=1978, prescriptions=[
            Prescription(drug_name = "adderall"),
            Prescription(drug_name = "setraline"),
            Prescription(drug_name = "lisinopril")
        ]),
        Patient(name="Lena Okafor", birth_year=1990, prescriptions=[
            Prescription(drug_name = "metformin")
        ]),
    ])
    session.commit()

# ─────────────────────────────────────────────────────────────
# YOUR RUNG-3 QUERY (the load-bearing bit — you write this):
# Using text(), select `name` and `birth_year` for every patient
# born after 1985, ordered by name. Use a BOUND PARAMETER for the
# year (:yr + a dict), never an f-string. Then loop and print each
# row as a tuple.
# ─────────────────────────────────────────────────────────────
with Session(engine) as session:
    result = session.execute(text("SELECT name, birth_year FROM patients WHERE birth_year > :yr ORDER BY name"), {"yr": 1985})
    for row in result:
        print(row)

    print()

    res = session.execute(text("SELECT name, drug_name, ROW_NUMBER() OVER (PARTITION BY prescriptions.patient_id ORDER BY rx_id) AS rx_num FROM prescriptions JOIN patients ON prescriptions.patient_id = patients.patient_id ORDER BY name"))
    for row in res:
        print(row)
