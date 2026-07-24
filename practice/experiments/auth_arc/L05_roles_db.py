from pydantic import BaseModel, ConfigDict
from sqlalchemy import String, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, sessionmaker
import bcrypt
from fastapi import FastAPI, HTTPException, status, Depends
import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
TOKEN_LIFETIME = timedelta(minutes=15)

app = FastAPI()


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id:              Mapped[int] = mapped_column(primary_key=True)
    username:        Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(60))
    role:            Mapped[str] = mapped_column(String(20), default="member")

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    role: str
    model_config = ConfigDict(from_attributes=True)


engine = create_engine("sqlite:///l05_roles.db")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    user = db.execute(
        select(User).where(User.username == payload["sub"])
    ).scalar_one_or_none()
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user


def require_role(*allowed: str):
    def validate(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in allowed:
            raise HTTPException(
                status_code = status.HTTP_403_FORBIDDEN,
                detail=f"You do not have permission to perform this action: Required role: {allowed}",
            )
        return current_user
    return validate

@app.post("/signup", response_model=UserOut, status_code = status.HTTP_201_CREATED)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=payload.username,
        hashed_password=hash_password(payload.password),
    )
    db.add(new_user)            # stage — no SQL yet
    try:
        db.commit()             # INSERT fires HERE — the only line that can blow
    except IntegrityError:
        db.rollback()           # reset the failed transaction
        raise HTTPException(status_code=409, detail="Username already taken")
    db.refresh(new_user)        # re-SELECT: pull the DB-assigned id onto the object
    return new_user             # ORM object → UserOut allow-list → envelope


@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.execute(              # ← THE REWIRE: dict lookup → SELECT
        select(User).where(User.username == form.username)
    ).scalar_one_or_none()
    if user is None or not bcrypt.checkpw(form.password.encode(), user.hashed_password.encode()):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    now = datetime.now(timezone.utc)
    token = jwt.encode(
        {"sub": user.username, "iat": now, "exp": now + TOKEN_LIFETIME},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return {"access_token": token, "token_type": "bearer"}


@app.get("/me", response_model=UserOut)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/notes")
def list_notes(current_user: User = Depends(get_current_user)):
    return {"notes": [], "viewer": current_user.username}


@app.get("/admin/users", response_model=list[UserOut])
def list_users(
        db: Session = Depends(get_db),
        admin: User = Depends(require_role("admin")),
):
    return db.execute(select(User)).scalars().all()

@app.get("/clinical/notes")
def list_clinical_notes(
        clinician: User = Depends(require_role("clinician")),
):
    return {"notes": [], "viewer": clinician.username}