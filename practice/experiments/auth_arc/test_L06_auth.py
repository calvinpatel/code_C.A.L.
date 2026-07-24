from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from fastapi.testclient import TestClient
from L05_roles_db import app, Base, get_db, User, hash_password

test_engine = create_engine(
    "sqlite:///test_auth.db",
    connect_args={"check_same_thread": False},
)
TestSessionLocal = sessionmaker(bind=test_engine)

def override_get_db():
    db = TestSessionLocal()
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


def test_signup_creates_member(client):
    r = client.post("/signup", json={"username": "test", "password": "password123"})
    assert r.status_code == 201
    assert r.json()["role"] == "member"

def test_login_returns_token(client):
    client.post("/signup", json={"username": "test", "password": "password123"})
    r = client.post("/login", data={"username": "test", "password": "password123"})
    assert r.status_code == 200
    assert "access_token" in r.json()

def test_me_requires_token(client):
    client.post("/signup", json={"username": "test", "password": "password123"})
    client.post("/login", data={"username": "test", "password": "password123"})
    r = client.get("/me")
    assert r.status_code == 401

def test_admin_route_forbidden_for_member(client):
    client.post("/signup", json={"username": "test", "password": "password123"})
    r = client.post("/login", data={"username": "test", "password": "password123"})
    token = r.json()["access_token"]
    r1 = client.get("/admin/users", headers={"Authorization": f"Bearer {token}"})
    assert r1.status_code == 403

def test_signup_ignores_role_field(client):
    r = client.post("/signup", json={"username": "test", "password": "password123", "role": "admin"})
    assert r.status_code == 201
    assert r.json()["role"] == "member"

def test_admin_route_allows_admin(client):
    # Create an admin user directly in the database
    with TestSessionLocal() as db:
        admin_user = User(
                username="admin",
                hashed_password=hash_password("adminpass"),
                role="admin"
            )
        db.add(admin_user)
        db.commit()

    # Login as admin
    r = client.post("/login", data={"username": "admin", "password": "adminpass"})
    token = r.json()["access_token"]

    # Access admin route
    r1 = client.get("/admin/users", headers={"Authorization": f"Bearer {token}"})
    assert r1.status_code == 200