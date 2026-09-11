from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import select
from sqlalchemy.orm import Session

from db import get_db
from models import Note
from schemas import NoteCreate, NoteOut, NoteList
from security import get_current_user

# routers/notes.py — the resource

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
    dependencies=[Depends(get_current_user)],
)

@router.post("", response_model=NoteOut, status_code=201)
def create_note(payload: NoteCreate, db: Session = Depends(get_db)):
    note = Note(**payload.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.get("", response_model=NoteList)
def list_notes(db: Session = Depends(get_db)):
    rows = db.scalars(select(Note)).all()
    return {"items": rows, "total": len(rows)}


@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.get(Note, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
