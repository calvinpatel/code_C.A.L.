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
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture()
def token(client):
    client.post("/api/v1/auth/signup", json={"username": "cal", "password": "hunter123"})
    r = client.post("/api/v1/auth/login", data={"username": "cal", "password": "hunter123"})
    assert r.status_code == 200
    return r.json()["access_token"]


def test_create_then_list(client, token):
    auth={"Authorization": f"Bearer {token}"}
    r = client.post("/api/v1/notes",
                    json={"title": "t", "body": "b"},
                    headers=auth,
                    )
    assert r.status_code == 201
    assert r.json()["id"] == 1
    assert client.get("/api/v1/notes", headers=auth).json() == {"items": [{"title": "t", "body": "b", "id": 1}],
                                                                "total": 1}


def test_list_starts_empty(client, token):
    auth={"Authorization": f"Bearer {token}"}
    assert client.get("/api/v1/notes", headers=auth).json() == {"items": [], "total": 0}


def test_404_shape(client, token):
    auth={"Authorization": f"Bearer {token}"}
    r = client.get("/api/v1/notes/999", headers=auth)
    assert r.status_code == 404
    assert set(r.json()) == {"detail"}


def test_422_strips_input(client, token):
    auth={"Authorization": f"Bearer {token}"}
    r = client.post("/api/v1/notes",
                    json={"title": "t"},
                    headers=auth,
                    )
    assert r.status_code == 422
    assert set(r.json()) == {"detail", "errors"}
    assert "input" not in r.text


def test_500_has_error_id():
    c = TestClient(app, raise_server_exceptions=False)
    r = c.get("/api/v1/boom")
    assert r.status_code == 500
    assert set(r.json()) == {"detail", "error_id"}


def test_json_login_is_422_envelope(client):
    r = client.post("api/v1/auth/login", json={"username": "cal", "password": "hunter123"})
    assert r.status_code == 422
    assert set(r.json()) == {"detail", "errors"}
    assert r.json()["detail"] == "Validation failed"


def test_tampered_token_is_401(client,token):
    auth={"Authorization": f"Bearer {token[:-4] + 'xxxx'}"}
    r = client.get("/api/v1/notes", headers=auth)
    assert r.status_code == 401
    assert r.json()["detail"] == "Invalid or expired token"