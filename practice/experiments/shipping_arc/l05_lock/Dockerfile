FROM python:3.14.3-slim
COPY --from=ghcr.io/astral-sh/uv:0.11.21 /uv /uvx /bin/

ENV UV_PYTHON_DOWNLOADS=0
WORKDIR /app

COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked --no-dev

COPY . .
ENV PATH="/app/.venv/bin:$PATH"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]