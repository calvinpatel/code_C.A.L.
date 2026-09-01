from pydantic import ConfigDict
from fastapi import FastAPI

from L03_request_body import NoteCreate

app = FastAPI()

class NoteOut(NoteCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int


@app.post("/notes", response_model=NoteOut)
def create_note(note: NoteCreate):
    # Simulate saving the note to a database and generating an ID
    saved_note = NoteOut(**note.model_dump(), id=1)  # Assigning a static ID for demonstration
    return saved_note