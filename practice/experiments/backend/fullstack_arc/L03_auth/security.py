from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy import select
from sqlalchemy.orm import Session

from config import get_settings
from db import get_db
from models import User

ALGORITHM = "HS256"
TOKEN_LIFETIME = timedelta(minutes=15)

# tokenUrl is documentation for /docs' Authorize button only; it must be the MOUNTED path
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


def create_access_token(username: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub": username, "iat": now, "exp": now + TOKEN_LIFETIME}
    return jwt.encode(payload, get_settings().secret_key, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, get_settings().secret_key, algorithms=[ALGORITHM])
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid or expired token",
                            headers={"WWW-Authenticate": "Bearer"})
    user = db.scalar(select(User).where(User.username == payload["sub"]))
    if user is None:
        raise HTTPException(status_code=401, detail="User no longer exists",
                            headers={"WWW-Authenticate": "Bearer"})
    return user