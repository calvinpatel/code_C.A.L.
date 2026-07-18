import time
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

class NoteCreate(BaseModel):
    title: str
    body: str


def write_audit_log(title:str):
    print("task starting")
    # raise ValueError("audit failed")
    time.sleep(2)           # pretend: slow I/O (email, external API)
    with open("audit_log", "a") as f:
        f.write(f"Note created: {title}\n")


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_audit_log, note.title)
    return {"saved": note.title}
