from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi.testclient import TestClient
from L04_users_db import app, engine, User

client = TestClient(app)

# r1 = client.post("/signup", json={"username": "cal", "password": "hunter2"})
# print("first signup:", r1.status_code, r1.json())
#
# r2 = client.post("/signup", json={"username": "cal", "password": "hunter3"})
# print("second signup:", r2.status_code, r2.json())
#
# r3 = client.post("/signup", json={"username": "cal"})
# print("third signup:", r3.status_code, r3.json())

client.post("/signup", json={"username": "cal", "password": "hunter2"})
r_login = client.post("/login", data={"username": "cal", "password": "hunter2"})
token = r_login.json()["access_token"]
print('login:', r_login.status_code, 'token starts:', token[:20] + '...')

"""Valid request"""
r_me = client.get("/me", headers={"Authorization": f"Bearer {token}"})
print("/me:", r_me.status_code, r_me.json())

"""naked request with no auth header"""
r_meh = client.get("/me")
print("/me:", r_meh.status_code, r_meh.json())

"""Tampered token"""
tampered = token[:-4] + "AAAA"
r_tamp = client.get("/me", headers={"Authorization": f"Bearer {tampered}"})
print("tampered token:", r_tamp.status_code, r_tamp.json())


"""Sign up, log in, delete user, hold token"""
client.post("/signup", json={"username": "bob", "password": "hunter1"})
r_user = client.post("/login", data={"username": "bob", "password": "hunter1"})
token_1 = r_user.json()["access_token"]

with Session(engine) as s:
    bob = s.execute(select(User).where(User.username == "bob")).scalar_one_or_none()
    s.delete(bob)
    s.commit()

r_gone = client.get("/me", headers={"Authorization": f"Bearer {token_1}"})
print("/me:", r_gone.status_code, r_gone.json())