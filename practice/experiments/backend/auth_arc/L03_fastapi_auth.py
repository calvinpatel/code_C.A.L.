import os
from dotenv import load_dotenv
import bcrypt
import jwt
from datetime import datetime, timezone, timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

load_dotenv()
SECRET_KEY = os.environ["SECRET_KEY"]        # fail-loud subscript — L2 habit
ALGORITHM = "HS256"
TOKEN_LIFETIME = timedelta(minutes=15)

app = FastAPI()

fake_users = {
    "cal": {
        "username": "cal",
        "hashed_password": bcrypt.hashpw(b"hunter2", bcrypt.gensalt()),
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = fake_users.get(form.username)
    if user is None or not bcrypt.checkpw(
        form.password.encode(), user["hashed_password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    now = datetime.now(timezone.utc)
    token = jwt.encode(
        {"sub": user["username"], "iat": now, "exp": now + TOKEN_LIFETIME},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return {"access_token": token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload["sub"]


@app.get("/protected")
def protected(current_user: str = Depends(get_current_user)):
    return {"message": f"Welcome, {current_user}. The vault is open."}