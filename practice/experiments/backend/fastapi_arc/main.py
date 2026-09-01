from fastapi import FastAPI

app = FastAPI()          # ← the framework object. Uvicorn will hold onto THIS.


# 🔴 YOUR KEYSTONE:
# Write one route handler for GET /health that returns {"status": "ok"}.
# Two pieces you need:
#   1. the decorator that REGISTERS the function on the app for GET at path "/health"
#      → it's a method on `app`, named after the HTTP verb. (callback: decorators arc)
#   2. a normal function under it that returns a plain Python dict.
# FastAPI turns that dict into JSON for you — you never touch json.dumps.

@app.get("/health")
def health():
    return {"status": "ok"}