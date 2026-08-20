from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class NoteIn(BaseModel):
    title: str
    author: str


# In-memory storage — resets every server restart (and --reload restarts on save).
notes = [
    {"id": 1, "title": "Chest pain follow-up", "author": "Dr. Osei"},
    {"id": 2, "title": "Diabetes check-in", "author": "Dr. Lin"},
    {"id": 3, "title": "Follow-up appointment, pt not alive", "author": "Dr. Escobal"},
    {"id": 4, "title": "Vax consultation, pt is a 2 yo child", "author": "Dr. Armah"},
]


@app.get("/notes")
def list_notes():
    return notes


@app.post("/notes")
def create_note(note: NoteIn):
    new = {"id": len(notes) + 1, "title": note.title, "author": note.author}
    notes.append(new)
    return new