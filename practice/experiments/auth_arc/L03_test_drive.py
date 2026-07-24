import time

import httpx

base = "http://127.0.0.1:8000"

r = httpx.post(f"{base}/login", data={"username": "cal", "password": "hunter3"})
print("1) wrong password ->", r.status_code, r.json())

r = httpx.post(f"{base}/login", data={"username": "cal", "password": "hunter2"})
print("2) correct login  ->", r.status_code)
token = r.json()["access_token"]
print("   token:", token[:40] + "...")

r = httpx.get(f"{base}/protected", headers={"Authorization": f"Bearer {token}"})
print("3) valid token    ->", r.status_code, r.json())

tampered = token[:-4] + "AAAA"
r = httpx.get(f"{base}/protected", headers={"Authorization": f"Bearer {tampered}"})
print("4) tampered token ->", r.status_code, r.json())

r = httpx.get(f"{base}/protected")
print("5) no authorization header ->", r.status_code, r.json())

r = httpx.post(f"{base}/login", json={"user": "cal", "password": "hunter2"})
print("6) wrong dialect ->", r.status_code, r.json())

time.sleep(6)
r = httpx.get(f"{base}/protected", headers={"Authorization": f"Bearer {token}"})
print("7) expired token -> ", r.status_code, r.json())