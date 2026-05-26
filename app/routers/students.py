"""Router para operaciones CRUD de estudiantes."""

from fastapi import APIRouter, HTTPException, status

from app.models.student import StudentCreate, StudentResponse, StudentUpdate
from app.storage.memory_store import student_store

router = APIRouter(prefix="/students", tags=["Students"])


@router.post(
    "",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un estudiante",
)
async def create_student(student: StudentCreate) -> StudentResponse:
    """Crea un nuevo estudiante en el sistema."""
    return student_store.create(student)


@router.get(
    "",
    response_model=list[StudentResponse],
    summary="Listar todos los estudiantes",
)
async def list_students() -> list[StudentResponse]:
    """Devuelve la lista completa de estudiantes."""
    return student_store.get_all()


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
    summary="Obtener un estudiante por ID",
)
async def get_student(student_id: str) -> StudentResponse:
    """Devuelve un estudiante específico por su ID."""
    student = student_store.get_by_id(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id '{student_id}' not found",
        )
    return student


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
    summary="Actualizar un estudiante",
)
async def update_student(student_id: str, data: StudentUpdate) -> StudentResponse:
    """Actualiza los campos de un estudiante existente."""
    student = student_store.update(student_id, data)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id '{student_id}' not found",
        )
    return student


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un estudiante",
)
async def delete_student(student_id: str) -> None:
    """Elimina un estudiante del sistema."""
    deleted = student_store.delete(student_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id '{student_id}' not found",
        )
