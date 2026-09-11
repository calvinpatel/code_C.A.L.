from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db import get_db
from models import User
from schemas import Token, UserCreate, UserPublic
from security import create_access_token, get_current_user, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=UserPublic, status_code=201)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    user = User(username=payload.username, hashed_password=hash_password(payload.password))
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Username already exists")
    db.refresh(user)
    return user


@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.username == form.username))
    if user is None or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    return {"access_token": create_access_token(user.username)}


@router.get("/me", response_model=UserPublic)
def me(current_user: User = Depends(get_current_user)):
    return current_user