"""Punto de entrada de la aplicación FastAPI.

Sistema CRUD básico para gestión de estudiantes con almacenamiento en memoria.
"""

from fastapi import FastAPI

from app.routers import health, students

app = FastAPI(
    title="Student Management API",
    description="API CRUD básica para gestión de estudiantes con almacenamiento local en memoria.",
    version="0.1.0",
)

# Registrar routers
app.include_router(health.router)
app.include_router(students.router)
