from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from db import get_db
from models import Note
from schemas import NoteCreate, NoteOut

# routers/notes.py — the resource

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("", response_model=NoteOut, status_code=201)
def create_note(payload: NoteCreate, db: Session = Depends(get_db)):
    note = Note(**payload.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.get("", response_model=list[NoteOut])
def list_notes(db: Session = Depends(get_db)):
    return db.scalars(select(Note)).all()