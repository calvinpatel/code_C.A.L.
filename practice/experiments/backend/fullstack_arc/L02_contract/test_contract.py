import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db import get_db
from main import app
from models import Base


@app.get("/api/v1/boom")
def boom():
    return 1/0


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
    r = client.post("/api/v1/notes", json={"title": "t", "body": "b"})
    assert r.status_code == 201
    assert r.json()["id"] == 1
    assert client.get("/api/v1/notes").json() == {"items": [{"title": "t", "body": "b", "id": 1}], "total": 1}


def test_list_starts_empty(client):
    assert client.get("/api/v1/notes").json() == {"items": [], "total": 0}


def test_404_shape(client):
    r = client.get("/api/v1/notes/999")
    assert r.status_code == 404
    assert set(r.json()) == {"detail"}


def test_422_strips_input(client):
    r = client.post("/api/v1/notes", json={"title": "t"})
    assert r.status_code == 422
    assert set(r.json()) == {"detail", "errors"}
    assert "input" not in r.text


def test_500_has_error_id():
    c = TestClient(app, raise_server_exceptions=False)
    r = c.get("/api/v1/boom")
    assert r.status_code == 500
    assert set(r.json()) == {"detail", "error_id"}

