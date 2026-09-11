import logging
import uuid

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from starlette.middleware.base import BaseHTTPMiddleware

# errors.py — the error contract. Defines handlers; installs nothing until asked.

log = logging.getLogger("app.errors")

async def validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
    errors = [
        {"field": ".".join(str(p) for p in e["loc"]), "msg": e["msg"]}
        for e in exc.errors()
    ]
    return JSONResponse(status_code=422, content={"detail": "Validation failed", "errors": errors})


def _envelope_500(request: Request) -> JSONResponse:
    error_id = uuid.uuid4().hex[:8]
    log.exception("Unhandled error %s on %s %s", error_id, request.method, request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Internal server error", "error_id": error_id})


class EnvelopeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception:
            return _envelope_500(request)


async def unhandled_errors(request: Request, exc: Exception) -> JSONResponse:
    return _envelope_500(request)


def install(app: FastAPI) -> None:
    app.add_middleware(EnvelopeMiddleware)
    app.add_exception_handler(RequestValidationError, validation_error)
    app.add_exception_handler(Exception, unhandled_errors)
