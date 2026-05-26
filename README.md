# Student Management API

API REST construida con **FastAPI** para gestión de estudiantes. Sistema CRUD básico con almacenamiento en memoria.

## Requisitos

- Python 3.12+

## Instalación

```bash
# Instalar dependencias de producción
pip install -r requirements.txt

# Instalar dependencias de desarrollo (incluye pytest)
pip install -r requirements-dev.txt
```

## Ejecución

```bash
uvicorn app.main:app --reload --port 8000
```

La documentación interactiva estará disponible en:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Endpoints

| Método   | Ruta                | Descripción                |
|----------|---------------------|----------------------------|
| `GET`    | `/health`           | Health check               |
| `GET`    | `/hello`            | Hello World                |
| `POST`   | `/students`         | Crear estudiante           |
| `GET`    | `/students`         | Listar todos               |
| `GET`    | `/students/{id}`    | Obtener por ID             |
| `PUT`    | `/students/{id}`    | Actualizar estudiante      |
| `DELETE` | `/students/{id}`    | Eliminar estudiante        |

## Tests

```bash
python -m pytest tests/ -v
```

## Estructura del Proyecto

```
app/
├── main.py                 # Entry point FastAPI
├── models/
│   └── student.py          # Schemas Pydantic
├── routers/
│   ├── health.py           # Health check y hello world
│   └── students.py         # CRUD de estudiantes
└── storage/
    └── memory_store.py     # Almacenamiento en memoria

tests/
├── test_health.py
└── test_students.py
```

## Licencia

Este proyecto es de uso interno y con fines de prueba.
