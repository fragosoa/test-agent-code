# Claude Context - Student Management API

## Descripción del Proyecto

API REST construida con **FastAPI** para gestión de estudiantes. Sistema CRUD básico con almacenamiento en memoria (in-memory). Diseñada como punto de partida para un proyecto que puede evolucionar hacia persistencia en base de datos.

## Comandos Útiles

```bash
# Instalar dependencias
pip install -r requirements.txt

# Instalar dependencias de desarrollo (incluye pytest)
pip install -r requirements-dev.txt

# Ejecutar la app en modo desarrollo
uvicorn app.main:app --reload --port 8000

# Ejecutar tests
python -m pytest tests/ -v

# Ver documentación interactiva (con la app corriendo)
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

## Estructura del Proyecto

```
app/
├── __init__.py
├── main.py                 # Entry point FastAPI, registro de routers
├── models/
│   ├── __init__.py
│   └── student.py          # Schemas Pydantic (Create, Update, Response)
├── routers/
│   ├── __init__.py
│   ├── health.py           # GET /health, GET /hello
│   └── students.py         # CRUD endpoints para /students
└── storage/
    ├── __init__.py
    └── memory_store.py     # Store en memoria (diccionario Python)

tests/
├── __init__.py
├── test_health.py          # Tests de health y hello world
└── test_students.py        # Tests CRUD de estudiantes
```

## Endpoints Disponibles

| Método   | Ruta                | Descripción                |
|----------|---------------------|----------------------------|
| `GET`    | `/health`           | Health check               |
| `GET`    | `/hello`            | Hello World                |
| `POST`   | `/students`         | Crear estudiante           |
| `GET`    | `/students`         | Listar todos               |
| `GET`    | `/students/{id}`    | Obtener por ID             |
| `PUT`    | `/students/{id}`    | Actualizar estudiante      |
| `DELETE` | `/students/{id}`    | Eliminar estudiante        |

## Convenciones de Código

- **Python 3.12+** requerido (usa `str | None` syntax)
- **Pydantic v2** para validación de datos
- **Conventional Commits** para mensajes de commit
- Tests con **pytest** y `TestClient` de FastAPI
- Cada test limpia el store (fixture `autouse=True`)

## Limitaciones Conocidas

- El almacenamiento es **en memoria**: los datos se pierden al reiniciar
- No hay autenticación ni autorización
- No hay validación de unicidad de email
- No hay paginación en el listado de estudiantes
