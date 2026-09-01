from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_db_check_reports_postgres_16():
    response = client.get("/db-check")
    assert response.status_code == 200
    assert response.json()["postgres"].startswith("PostgreSQL 16")