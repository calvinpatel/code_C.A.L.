from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

app = FastAPI()

# a DEPENDENCY: a plain function FastAPI runs BEFORE the handler.
# note it has its OWN params — FastAPI resolves them from the query string, exactly like L2.
def pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

def note_filters(priority: int| None = None, tag: str | None = None ) -> dict:
    return {"priority": priority, "tag": tag}

@app.get("/notes")
def list_notes(page: dict = Depends(pagination)):   # inject pagination's RESULT as `page`
    return {"you_asked_for": page}

@app.get("/tags")
def list_tags(page: dict = Depends(pagination)):    # SAME dependency, reused — zero copy-paste
    return {"tags_page": page}

@app.get("/notes/search")
def list_notes_search(filters: dict = Depends(note_filters)):
    return {"filters": filters}

client = TestClient(app)
print("defaults   ->", client.get("/notes").json())
print("with query ->", client.get("/notes?skip=20&limit=5").json())
print("reused     ->", client.get("/tags?skip=99").json())
print("search filter ->", client.get("/notes/search?priority=1&tag=sepsis").json())
print("search filter default ->", client.get("/notes/search").json())