import time

import bcrypt

password = b"hunter2"          # bcrypt works on bytes, not str

# --- Signup: hash the same password twice ---
hash_1 = bcrypt.hashpw(password, bcrypt.gensalt())   # gensalt() -> fresh random salt
hash_2 = bcrypt.hashpw(password, bcrypt.gensalt())

print("hash_1:", hash_1.decode())
print("hash_2:", hash_2.decode())
print("identical?", hash_1 == hash_2)

# --- Login: verify a candidate against a stored hash ---
print("right pw vs hash_1:", bcrypt.checkpw(b"hunter2", hash_1))
print("right pw vs hash_2:", bcrypt.checkpw(b"hunter2", hash_2))
print("wrong pw vs hash_1:", bcrypt.checkpw(b"hunter3", hash_1))

# --- The work factor, felt ---
for cost in (4, 12):
    start = time.perf_counter()
    bcrypt.hashpw(password, bcrypt.gensalt(rounds=cost))
    print(f"cost {cost:2d}: {time.perf_counter() - start:.3f}s per hash")