from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Patient(Base):
    __tablename__ = "patients"

    patient_id: Mapped[int] = mapped_column(primary_key=True)
    name:       Mapped[str] = mapped_column()
    birth_year: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"Patient(patient_id={self.patient_id}, name={self.name!r}, birth_year={self.birth_year})"


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    # 1. build the three Patient objects: Ava Chen (1991), Marcus Reid (1978), Lena Okafor (2002)
    #    — no patient_id; the DB assigns it
    ava = Patient(name="Ava Chen", birth_year=1991)
    marcus = Patient(name="Marcus Reid", birth_year=1978)
    lena = Patient(name="Lena Okafor", birth_year=2002)
    # 2. PREDICT, then print: what is marcus.patient_id BEFORE commit?
    print(f"Before: {marcus.patient_id}")
    # 3. stage them   (three session.add(...) calls, or one session.add_all([...]))
    session.add_all([ava, marcus, lena])
    # 4. commit
    session.commit()
    # 5. print marcus.patient_id AFTER commit — did your prediction hold?
    print(f"After: {marcus.patient_id}")
    # 6. fetch patient #2 by primary key, print just their name
    fetched = session.get(Patient, 2)
    print(fetched.name)
    # 7. fetch #2 a SECOND time; prove the identity map with `is`
    first = session.get(Patient, 2)
    second = session.get(Patient, 2)
    print(first is second)