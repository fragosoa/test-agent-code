"""Tests para los endpoints de health y hello world."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    """GET /health debe devolver status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "message" in data


def test_hello_world():
    """GET /hello debe devolver Hello, World!."""
    response = client.get("/hello")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, World!"
