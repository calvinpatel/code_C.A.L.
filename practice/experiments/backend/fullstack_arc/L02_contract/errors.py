import logging
import uuid

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

# errors.py — the error contract. Defines handlers; installs nothing until asked.

log = logging.getLogger("app.errors")

async def validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
    errors = [
        {"field": ".".join(str(p) for p in e["loc"]), "msg": e["msg"]}
        for e in exc.errors()
    ]
    return JSONResponse(status_code=422, content={"detail": "Validation failed", "errors": errors})


async def unhandled_errors(request: Request, exc: Exception) -> JSONResponse:
    error_id = uuid.uuid4().hex[:8]
    log.exception("Unhandled error %s on %s %s", error_id, request.method, request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Internal server error", "error_id": error_id})


def install(app: FastAPI) -> None:
    app.add_exception_handler(RequestValidationError, validation_error)
    app.add_exception_handler(Exception, unhandled_errors)
