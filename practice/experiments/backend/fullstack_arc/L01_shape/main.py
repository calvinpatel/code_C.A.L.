from fastapi import FastAPI
from routers import notes

# main.py — the composition root. Five lines, and it stays five lines.

app = FastAPI()
app.include_router(notes.router)