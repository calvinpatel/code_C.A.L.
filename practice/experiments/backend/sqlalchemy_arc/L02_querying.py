from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Patient(Base):
    __tablename__ = "patients"

    patient_id: Mapped[int] = mapped_column(primary_key=True)
    name:       Mapped[str] = mapped_column()
    birth_year: Mapped[int] = mapped_column()
    site:       Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Patient(patient_id={self.patient_id}, name={self.name!r}, birth_year={self.birth_year}, site={self.site!r})"


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([
        Patient(name="Ava Chen",    birth_year=1991, site="Baltimore"),
        Patient(name="Marcus Reid", birth_year=1978, site="Baltimore"),
        Patient(name="Lena Okafor", birth_year=2002, site="Bethesda"),
        Patient(name="Sam Park",    birth_year=1995, site="Baltimore"),
        Patient(name="Tariq Bell",  birth_year=1988, site="Bethesda"),
        Patient(name="Nora Diaz",   birth_year=2000, site="Baltimore"),
    ])
    session.commit()

    print("\n── Query A: born before 2000, ordered by name A→Z ──")
    #    (your select / where / order_by / scalars here)
    stmt = select(Patient).where(Patient.birth_year < 2000).order_by(Patient.name)
    for p in session.scalars(stmt).all():
        print(p.name)

    print("\n── Query B: the single oldest patient ──")
    #    (your select / order_by / consumer here)
    oldest = select(Patient).order_by(Patient.birth_year).limit(1)
    for p in session.scalars(oldest).all():
        print(p.name)

    print("\n── Query C: average birth year per site ──")
    avg_year = select(Patient.site, func.avg(Patient.birth_year).label("avg")).group_by(Patient.site)
    for row in session.execute(avg_year).all():
        print(row.site, "->", row.avg)

    print("\n── Query D: patients born in or after 1990, as a single number ──")
    boomers = select(func.count(Patient.patient_id)).where(Patient.birth_year >= 1990)
    print(session.scalar(boomers))

