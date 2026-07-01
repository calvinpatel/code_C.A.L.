from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Patient(Base):
    __tablename__ = "patients"
    patient_id:    Mapped[int] = mapped_column(primary_key=True)
    name:          Mapped[str] = mapped_column()
    birth_year:    Mapped[int | None] = mapped_column()
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