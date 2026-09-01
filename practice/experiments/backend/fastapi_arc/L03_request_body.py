from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NoteCreate(BaseModel):
    title: str
    body: str
    priority: int = 1
    tags: list[str] = []

    # tags: list[str] = Field(default_factory=list)  <- explicit, make a new list per instance (import Field from pydantic)

@app.post("/notes")
def create_note(note: NoteCreate):
    return {"received": note.model_dump()}  # model_dump() returns a dict of the model's data


