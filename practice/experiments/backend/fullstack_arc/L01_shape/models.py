from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# models.py — ORM tables. Also imports nothing from the project.

class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    body: Mapped[str]