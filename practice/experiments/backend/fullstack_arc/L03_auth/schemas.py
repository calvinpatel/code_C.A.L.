from pydantic import BaseModel, ConfigDict

# schemas.py — the spine. Imports nothing from the project.

class NoteCreate(BaseModel):
    title: str
    body: str


class NoteOut(NoteCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class NoteList(BaseModel):
    items: list[NoteOut]
    total: int


class UserCreate(BaseModel):
    username: str
    password: str


class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"