import jwt
from datetime import datetime, timedelta, timezone
import base64
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

payload = {
    "sub": "cal",
    "iat": datetime.now(timezone.utc),
    "exp": datetime.now(timezone.utc) + timedelta(minutes=15),
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("TOKEN:", token)
print()

decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
print("decoded:", decoded)

header_seg, payload_seg, signature_seg = token.split(".")

# base64 requires length divisible by 4; JWT strips the "=" padding chars
# to stay URL-safe. (-len % 4) computes exactly how many "=" to restore:
# in Python, -10 % 4 == 2  (result always takes the sign of the divisor)
padded = payload_seg + "=" * (-len(payload_seg) % 4)

print(base64.urlsafe_b64decode(padded))