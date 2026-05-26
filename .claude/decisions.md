# Decisiones de Arquitectura y Diseño

> Registro de decisiones tomadas durante el desarrollo del proyecto.
> Cada decisión incluye contexto, opciones consideradas y justificación.

---

## 001 - Framework: FastAPI

**Fecha:** 2026-05-26
**Estado:** Aceptada

**Contexto:** Se necesita un framework web para Python que soporte una API REST.

**Decisión:** Usar FastAPI.

**Justificación:**
- Validación automática con Pydantic
- Documentación OpenAPI auto-generada (Swagger UI + ReDoc)
- Soporte nativo para async
- Tipado fuerte con type hints de Python
- Alto rendimiento

---

## 002 - Almacenamiento en memoria (diccionario Python)

**Fecha:** 2026-05-26
**Estado:** Aceptada (temporal)

**Contexto:** Se necesita un mecanismo de almacenamiento para el CRUD de estudiantes. El requerimiento indica "storage local".

**Opciones consideradas:**
1. Diccionario en memoria (Python `dict`)
2. SQLite con SQLAlchemy
3. Archivo JSON en disco

**Decisión:** Diccionario en memoria con una clase `MemoryStore`.

**Justificación:**
- Máxima simplicidad para un MVP
- Sin dependencias externas de base de datos
- Fácil de reemplazar por una implementación con DB real
- El store es una clase con interfaz clara (`create`, `get_all`, `get_by_id`, `update`, `delete`) que actúa como repositorio

**Trade-offs:**
- Los datos se pierden al reiniciar la app
- No apto para producción con múltiples workers (cada worker tendría su propio store)

---

## 003 - UUID como identificador de estudiantes

**Fecha:** 2026-05-26
**Estado:** Aceptada

**Contexto:** Se necesita un mecanismo para generar IDs únicos para estudiantes.

**Opciones consideradas:**
1. UUID v4 (aleatorio)
2. Auto-incremental entero
3. ULID o NanoID

**Decisión:** UUID v4 usando `uuid.uuid4()`.

**Justificación:**
- Viene incluido en la librería estándar de Python
- Universalmente único, sin necesidad de coordinación
- Preparado para migración futura a base de datos distribuida

---

## 004 - Separación en routers por dominio

**Fecha:** 2026-05-26
**Estado:** Aceptada

**Contexto:** Definir cómo organizar los endpoints.

**Decisión:** Un router por dominio funcional:
- `health.py` → endpoints de infraestructura (`/health`, `/hello`)
- `students.py` → CRUD de estudiantes (`/students/*`)

**Justificación:**
- Separación clara de responsabilidades
- Escalable: agregar nuevas entidades = agregar nuevo router
- Facilita testing aislado

---

## 005 - Schemas Pydantic separados por operación

**Fecha:** 2026-05-26
**Estado:** Aceptada

**Contexto:** Cómo definir los modelos de datos para request/response.

**Decisión:** Tres schemas separados:
- `StudentCreate` → campos requeridos para creación
- `StudentUpdate` → todos los campos opcionales (partial update)
- `StudentResponse` → incluye el `id` generado

**Justificación:**
- Validación precisa según la operación
- Permite updates parciales sin requerir todos los campos
- El response siempre incluye el ID, el create nunca lo pide
