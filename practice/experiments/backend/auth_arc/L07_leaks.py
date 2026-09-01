import logging
import uuid

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from starlette.responses import JSONResponse

logging.basicConfig(level=logging.ERROR, format="%(levelname)s %(message)s")
logger = logging.getLogger("app")

app = FastAPI()


def process_note(text: str) -> dict:
    # Stand-in for the real pipeline; the DB driver dies mid-write,
    # and its exception message carries the data it was touching.
    raise RuntimeError(
        f"INSERT failed for row (patient='Maria Gonzalez', dx='HIV+'): disk full — note was: {text!r}"
    )


@app.post("/leaky")
def leaky(payload: dict):
    try:
        return process_note(payload["text"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   # 🔴 THE LEAK


@app.post("/sealed")
def sealed(payload: dict):
    return process_note(payload["text"])   # no try — let it escape to the net


@app.exception_handler(Exception)
def sanitize_unhandled(request, exc):
    incident_id = uuid.uuid4().hex[:8]                        # mint the claim ticket
    logger.error("incident=%s %s: %s", incident_id, type(exc).__name__, exc)  # full truth, server side
    return JSONResponse(                                      # generic verdict, client side
        status_code=500,
        content={"detail": "Internal server error", "incident_id": incident_id},
    )


client = TestClient(app, raise_server_exceptions=False)

r = client.post("/leaky", json={"text": "45yo M, chest pain..."})
print("LEAKY  ->", r.status_code, r.json())

r = client.post("/sealed", json={"text": "45yo M, chest pain..."})
print("SEALED ->", r.status_code, r.json())