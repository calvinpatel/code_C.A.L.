from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import errors
from routers import notes
from config import get_settings


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_settings().cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
errors.install(app)
app.include_router(notes.router, prefix="/api/v1")