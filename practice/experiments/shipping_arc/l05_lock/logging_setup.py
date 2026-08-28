import json
import logging
import sys
from datetime import datetime, timezone
import traceback
from pathlib import Path

APP_ROOT = str(Path(__file__).resolve().parent)


class JsonFormatter(logging.Formatter):
    def __init__(self, app_root: str = APP_ROOT) -> None:
        super().__init__()
        self.app_root = app_root

    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        ctx = getattr(record, "ctx", None)
        if ctx:
            payload.update(ctx)
        if record.name == "uvicorn.access":
            assert isinstance(record.args, tuple)
            payload["client"] = record.args[0]
            payload["method"] = record.args[1]
            payload["path"] = record.args[2]
            payload["status"] = record.args[4]
        if record.exc_info:
            exc_type, exc_value, tb = record.exc_info
            payload["exc_type"] = exc_type.__name__
            payload["exc_msg"] = "".join(traceback.format_exception_only(exc_type, exc_value)).strip()
            frames = traceback.extract_tb(tb)
            app_frames = [f for f in frames if f.filename.startswith(self.app_root)]
            payload["exc_frames"] = [f"{f.filename}:{f.lineno} in {f.name}" for f in app_frames]
            payload["exc_depth"] = len(frames)
            cause = exc_value.__cause__
            if cause is not None:
                payload["exc_cause"] = "".join(traceback.format_exception_only(type(cause), cause)).strip()
        return json.dumps(payload)


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {"()": "logging_setup.JsonFormatter"},
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "json",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["stdout"], "level": "INFO", "propagate": False},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["stdout"], "level": "INFO", "propagate": False},
    },
    "root": {"handlers": ["stdout"], "level": "INFO"},
}