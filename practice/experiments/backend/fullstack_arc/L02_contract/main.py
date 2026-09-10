from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import errors
from routers import notes
from config import get_settings


app = FastAPI()
errors.install(app)     # add_middleware wraps outward; the envelope catcher must sit inside CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_settings().cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(notes.router, prefix="/api/v1")

@app.get("/api/v1/boom")
async def boom():
    raise RuntimeError("kaboom")