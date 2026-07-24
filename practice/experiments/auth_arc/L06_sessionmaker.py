from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine("sqlite:///l06_demo.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)

Base.metadata.create_all(engine)

# ---- the factory, configured ONCE at boot ----
SessionLocal = sessionmaker(bind=engine)

# ---- products, manufactured per use ----
s1 = SessionLocal()
s2 = SessionLocal()

print(type(SessionLocal).__name__)          # what IS the factory?
print(type(s1).__name__, type(s2).__name__) # what does it manufacture?
print(s1 is s2)                             # distinct products?
print(s1.get_bind() is engine)              # config carried inside?

with SessionLocal() as db:
    db.add(User(username="cal"))
    db.commit()

with SessionLocal() as db:
    print(db.execute(select(User.username)).scalars().all())