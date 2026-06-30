from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column, Session, selectinload


class Base(DeclarativeBase):
    pass

class Patient(Base):
    __tablename__ = "patients"
    patient_id:    Mapped[int] = mapped_column(primary_key=True)
    name:          Mapped[str] = mapped_column()
    prescriptions: Mapped[list["Prescription"]] = relationship(back_populates="patient")

    def __repr__(self) -> str:
        return f"Patient(patient_id={self.patient_id}, name={self.name!r})"

class Prescription(Base):
    __tablename__ = "prescriptions"
    rx_id:      Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.patient_id"))
    drug_name:  Mapped[str] = mapped_column()
    patient:    Mapped["Patient"] = relationship(back_populates="prescriptions")

    def __repr__(self) -> str:
        return f"Prescription(rx_id={self.rx_id}, patient_id={self.patient_id}, drug_name={self.drug_name!r})"

engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([
        Patient(name="Ava Chen", prescriptions=[
            Prescription(drug_name="amoxicillin"),
            Prescription(drug_name="lisinopril"),
        ]),
        Patient(name="Marcus Reid", prescriptions=[
            Prescription(drug_name="metformin"),
        ]),
        Patient(name="Lena Okafor", prescriptions=[
            Prescription(drug_name="adderall"),
            Prescription(drug_name="vancomycin")
        ]),
        Patient(name="Jessica Winters", prescriptions=[])
    ])
    session.commit()

    print("Task 1")
    for p in session.scalars(select(Patient)).all():
        print(f"{p.name}: {len(p.prescriptions)} prescriptions")

    print("\nTask 2")
    fetched = session.get(Prescription, 1)
    print(fetched.drug_name, "->", fetched.patient.name)

    print("\nTask 3")
    for p in session.scalars(select(Patient).options(selectinload(Patient.prescriptions))).all():
        print(p.name, len(p.prescriptions))
