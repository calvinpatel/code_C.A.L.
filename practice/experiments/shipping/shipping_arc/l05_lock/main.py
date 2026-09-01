import logging
import uuid

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from sqlalchemy import text
from db import engine

log = logging.getLogger("notepilot.api")
app = FastAPI()


@app.exception_handler(Exception)
async def unhandled(request: Request, exc: Exception) -> JSONResponse:
    error_id = uuid.uuid4().hex
    log.exception(
        "unhandled exception",
        extra={"ctx": {
            "error_id": error_id,
            "method": request.method,
            "path": request.url.path,
        }},
    )
    return JSONResponse(
        status_code=500,
        content={"detail": "internal error", "error_id": error_id},
    )


@app.get("/")
def root():
    return {"status": "alive", "from": "inside the box"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version()")).scalar()
    return {"postgres": version}