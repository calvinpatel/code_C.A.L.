import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db import get_db
from main import app
from models import Base

test_engine = create_engine("sqlite:///test_notes.db",
                            connect_args={"check_same_thread": False})


def override_get_db():
    db = Session(test_engine)
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client():
    Base.metadata.drop_all(test_engine)
    Base.metadata.create_all(test_engine)
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_create_then_list(client):
    r = client.post("/notes", json={"title": "t", "body": "b"})
    assert r.status_code == 201
    assert r.json()["id"] == 1
    assert client.get("/notes").json() == [{"title": "t", "body": "b", "id": 1}]

def test_list_starts_empty(client):
    assert client.get("/notes").json() == []