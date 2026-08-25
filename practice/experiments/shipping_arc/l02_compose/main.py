from fastapi import FastAPI
from sqlalchemy import text
from db import engine

app = FastAPI()

@app.get("/")
def root():
    return {"status": "alive", "from": "inside the box"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version()")).scalar()
    return {"postgres": version}