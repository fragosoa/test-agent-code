"""Almacenamiento en memoria para estudiantes.

Usa un diccionario en memoria como store. Los datos se pierden
al reiniciar la aplicación. Ideal para desarrollo y pruebas.
"""

import uuid

from app.models.student import StudentCreate, StudentResponse, StudentUpdate


class MemoryStore:
    """Store en memoria para operaciones CRUD de estudiantes."""

    def __init__(self) -> None:
        self._students: dict[str, dict] = {}

    def create(self, student: StudentCreate) -> StudentResponse:
        """Crea un nuevo estudiante y devuelve su representación."""
        student_id = str(uuid.uuid4())
        record = {
            "id": student_id,
            "name": student.name,
            "email": student.email,
            "age": student.age,
            "major": student.major,
        }
        self._students[student_id] = record
        return StudentResponse(**record)

    def get_all(self) -> list[StudentResponse]:
        """Devuelve todos los estudiantes."""
        return [StudentResponse(**s) for s in self._students.values()]

    def get_by_id(self, student_id: str) -> StudentResponse | None:
        """Devuelve un estudiante por ID, o None si no existe."""
        record = self._students.get(student_id)
        if record is None:
            return None
        return StudentResponse(**record)

    def update(self, student_id: str, data: StudentUpdate) -> StudentResponse | None:
        """Actualiza un estudiante existente. Devuelve None si no existe."""
        record = self._students.get(student_id)
        if record is None:
            return None

        update_fields = data.model_dump(exclude_unset=True)
        for key, value in update_fields.items():
            record[key] = value

        self._students[student_id] = record
        return StudentResponse(**record)

    def delete(self, student_id: str) -> bool:
        """Elimina un estudiante. Devuelve True si existía, False si no."""
        if student_id in self._students:
            del self._students[student_id]
            return True
        return False

    def count(self) -> int:
        """Devuelve la cantidad de estudiantes almacenados."""
        return len(self._students)


# Instancia global (singleton) del store
student_store = MemoryStore()
