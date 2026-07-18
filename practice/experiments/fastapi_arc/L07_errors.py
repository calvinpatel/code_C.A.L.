from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app, raise_server_exceptions=False)

NOTES = {
    1: {"title": "ward round", "body": "pt stable overnight"},
    2: {"title": "discharge plan", "body": "home with PT follow-up"},
}

# --- the "before" picture: no error handling at all ---
@app.get("/crash/{note_id}")
def get_note_crash(note_id: int):
    return NOTES[note_id]          # KeyError when the id is absent

# --- the honest version ---
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id not in NOTES:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")
    return NOTES[note_id]


r = client.get("/crash/99")
print(r.status_code, repr(r.text))

r = client.get("/notes/1")
print(r.status_code, r.json())

r = client.get("/notes/99")
print(r.status_code, r.json())

r = client.get("/notes/abc")
print(r.status_code, r.json()["detail"][0]["loc"], r.json()["detail"][0]["type"])

r = client.get("/crash/1")
print(r.status_code, r.json())