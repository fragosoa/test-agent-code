"""Modelos Pydantic para la entidad Student."""

from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    """Schema para crear un estudiante."""

    name: str = Field(..., min_length=1, max_length=100, description="Nombre del estudiante")
    email: str = Field(..., min_length=5, max_length=150, description="Email del estudiante")
    age: int = Field(..., ge=1, le=150, description="Edad del estudiante")
    major: str | None = Field(None, max_length=100, description="Carrera o especialidad")


class StudentUpdate(BaseModel):
    """Schema para actualizar un estudiante (todos los campos opcionales)."""

    name: str | None = Field(None, min_length=1, max_length=100, description="Nombre del estudiante")
    email: str | None = Field(None, min_length=5, max_length=150, description="Email del estudiante")
    age: int | None = Field(None, ge=1, le=150, description="Edad del estudiante")
    major: str | None = Field(None, max_length=100, description="Carrera o especialidad")


class StudentResponse(BaseModel):
    """Schema de respuesta para un estudiante."""

    id: str = Field(..., description="Identificador único del estudiante")
    name: str = Field(..., description="Nombre del estudiante")
    email: str = Field(..., description="Email del estudiante")
    age: int = Field(..., description="Edad del estudiante")
    major: str | None = Field(None, description="Carrera o especialidad")
