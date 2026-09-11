from contextlib import asynccontextmanager

from sqlalchemy import text

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import errors
from routers import notes, auth
from config import get_settings
from db import get_engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_settings()
    with get_engine().connect() as conn:
        conn.execute(text("SELECT 1"))
    print("startup checks passed")
    yield
    get_engine().dispose()
    print("engine disposed")

app = FastAPI(lifespan=lifespan)
errors.install(app)     # add_middleware wraps outward; the envelope catcher must sit inside CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_settings().cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(notes.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")

@app.get("/api/v1/boom")
async def boom():
    raise RuntimeError("kaboom")