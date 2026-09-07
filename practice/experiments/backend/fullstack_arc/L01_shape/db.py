from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import get_settings

# db.py — the engine, built on first use

@lru_cache
def get_engine():
    return create_engine(get_settings().database_url)


def get_db():
    db = Session(get_engine())
    try:
        yield db
    finally:
        db.close()