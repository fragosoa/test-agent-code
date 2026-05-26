"""Tests para los endpoints CRUD de estudiantes."""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.storage.memory_store import student_store

client = TestClient(app)


@pytest.fixture(autouse=True)
def _clear_store():
    """Limpia el store antes de cada test para evitar estado compartido."""
    student_store._students.clear()
    yield
    student_store._students.clear()


SAMPLE_STUDENT = {
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "age": 21,
    "major": "Ingeniería de Software",
}


class TestCreateStudent:
    """Tests para POST /students."""

    def test_create_student_success(self):
        response = client.post("/students", json=SAMPLE_STUDENT)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == SAMPLE_STUDENT["name"]
        assert data["email"] == SAMPLE_STUDENT["email"]
        assert data["age"] == SAMPLE_STUDENT["age"]
        assert data["major"] == SAMPLE_STUDENT["major"]
        assert "id" in data

    def test_create_student_without_major(self):
        payload = {"name": "Ana López", "email": "ana@example.com", "age": 20}
        response = client.post("/students", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["major"] is None

    def test_create_student_invalid_data(self):
        payload = {"name": "", "email": "bad", "age": -1}
        response = client.post("/students", json=payload)
        assert response.status_code == 422


class TestListStudents:
    """Tests para GET /students."""

    def test_list_empty(self):
        response = client.get("/students")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_after_create(self):
        client.post("/students", json=SAMPLE_STUDENT)
        client.post("/students", json={**SAMPLE_STUDENT, "name": "María", "email": "maria@example.com"})
        response = client.get("/students")
        assert response.status_code == 200
        assert len(response.json()) == 2


class TestGetStudent:
    """Tests para GET /students/{id}."""

    def test_get_existing(self):
        create_resp = client.post("/students", json=SAMPLE_STUDENT)
        student_id = create_resp.json()["id"]
        response = client.get(f"/students/{student_id}")
        assert response.status_code == 200
        assert response.json()["id"] == student_id

    def test_get_not_found(self):
        response = client.get("/students/nonexistent-id")
        assert response.status_code == 404


class TestUpdateStudent:
    """Tests para PUT /students/{id}."""

    def test_update_success(self):
        create_resp = client.post("/students", json=SAMPLE_STUDENT)
        student_id = create_resp.json()["id"]
        response = client.put(f"/students/{student_id}", json={"name": "Juan Actualizado"})
        assert response.status_code == 200
        assert response.json()["name"] == "Juan Actualizado"
        # Los demás campos no cambian
        assert response.json()["email"] == SAMPLE_STUDENT["email"]

    def test_update_not_found(self):
        response = client.put("/students/nonexistent-id", json={"name": "X"})
        assert response.status_code == 404


class TestDeleteStudent:
    """Tests para DELETE /students/{id}."""

    def test_delete_success(self):
        create_resp = client.post("/students", json=SAMPLE_STUDENT)
        student_id = create_resp.json()["id"]
        response = client.delete(f"/students/{student_id}")
        assert response.status_code == 204
        # Verificar que ya no existe
        get_resp = client.get(f"/students/{student_id}")
        assert get_resp.status_code == 404

    def test_delete_not_found(self):
        response = client.delete("/students/nonexistent-id")
        assert response.status_code == 404
