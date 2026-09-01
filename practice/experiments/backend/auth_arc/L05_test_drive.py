import bcrypt
from fastapi.testclient import TestClient
from L05_roles_db import app, User, SessionLocal

client = TestClient(app)

# Seed the admin SERVER-SIDE — power never enters through the signup door
with SessionLocal as db:
    db.add(User(
        username="root",
        hashed_password=bcrypt.hashpw(b"rootpw", bcrypt.gensalt()).decode(),
        role= "admin"
    ))
    db.commit()


# An ordinary member arrives through the front door
r = client.post("/signup", json={"username": "cal", "password": "hunter2"})
print("signup cal:", r.status_code, r.json())

def login(username, password):
    r = client.post("/login", data={"username": username, "password": password})
    return r.json()["access_token"]

cal_token = login(username="cal", password="hunter2")
root_token = login(username="root", password="rootpw")

r = client.get("/notes", headers={"Authorization": f"Bearer {cal_token }"})
print("cal -> /notes:", r.status_code, r.json())

r = client.get("/admin/users", headers={"Authorization": f"Bearer {root_token}"})
print("root -> /admin/users:", r.status_code, r.json())


"""Unauthorized user accessing admin only path"""
r = client.get("/admin/users", headers={"Authorization": f"Bearer {cal_token}"})
print("cal -> /admin/users:", r.status_code, r.json())


"""No Authorization header, valid admin user"""
r = client.get("/admin/users")
print("no header root -> /admin/users:", r.status_code, r.json())


"""Tampered token, valid admin user"""
tampered_token = root_token[:-4] + "AAAA"
r = client.get("/admin/users", headers={"Authorization": f"Bearer {tampered_token}"})
print("tampered admin -> /admin/users:", r.status_code, r.json())


"""Attacker signup as admin"""
r = client.post("/signup", json={"username": "eve", "password": "x", "role": "admin"})
print("bypass default role:", r.status_code, r.json())


"""Admin accessing something needing a clinician role"""
r = client.get("/clinical/notes", headers={"Authorization": f"Bearer {root_token}"})
print("root -> /clinical/notes:", r.status_code, r.json())


""""Normal user accessing clinician notes"""
r = client.get("/clinical/notes", headers={"Authorization": f"Bearer {cal_token}"})
print("cal -> /clinical/notes:", r.status_code, r.json())