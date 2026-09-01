from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NoteIn(BaseModel):
    patient_id: str
    text: str

@app.post("/summarize")
def summarize(note: NoteIn):
    return {
        "patient_id": note.patient_id,
        "word count": len(note.text.split()),
        "summary": f"[stub] first 5 words: {' '.join(note.text.split()[:5])}",
    }