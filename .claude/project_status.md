# Estado del Proyecto

> Última actualización: Task #9

---

## Resumen General

| Aspecto            | Estado          |
|--------------------|-----------------|
| Framework          | FastAPI 0.115   |
| Python             | 3.12+           |
| Tests              | 13 passing ✅   |
| Almacenamiento     | In-memory       |
| Autenticación      | ❌ No implementada |
| Base de datos      | ❌ No implementada |
| Docker             | ❌ No implementado |
| CI/CD              | ❌ No implementado |

---

## Features Implementadas

### Task #9 - App básica FastAPI con CRUD de estudiantes
- [x] Endpoint `GET /health` (health check)
- [x] Endpoint `GET /hello` (hello world)
- [x] `POST /students` - Crear estudiante
- [x] `GET /students` - Listar estudiantes
- [x] `GET /students/{id}` - Obtener estudiante por ID
- [x] `PUT /students/{id}` - Actualizar estudiante
- [x] `DELETE /students/{id}` - Eliminar estudiante
- [x] Modelos Pydantic con validación
- [x] Almacenamiento en memoria (MemoryStore)
- [x] Tests completos (13 tests)
- [x] Archivos de contexto Claude

---

## Backlog / Mejoras Futuras

- [ ] Agregar persistencia con SQLite + SQLAlchemy
- [ ] Agregar autenticación (JWT)
- [ ] Agregar paginación al listado
- [ ] Validación de email único
- [ ] Dockerfile y docker-compose
- [ ] CI/CD con GitHub Actions
- [ ] Logging estructurado
- [ ] Variables de entorno con pydantic-settings
- [ ] Manejo centralizado de errores
- [ ] Búsqueda/filtrado de estudiantes

---

## Dependencias del Proyecto

### Producción (`requirements.txt`)
| Paquete   | Versión   | Propósito                    |
|-----------|-----------|------------------------------|
| fastapi   | 0.115.12  | Framework web                |
| uvicorn   | 0.34.3    | Servidor ASGI                |
| pydantic  | 2.11.3    | Validación y serialización   |

### Desarrollo (`requirements-dev.txt`)
| Paquete   | Versión   | Propósito       |
|-----------|-----------|-----------------|
| pytest    | 8.4.1     | Test runner     |
| httpx     | 0.28.1    | HTTP client (requerido por TestClient) |
