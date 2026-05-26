# Dependency Graph

> Generado automáticamente por análisis estático de imports · 2026-05-26 06:36 UTC
> Una arista A → B significa 'A importa B'.
> Actualizado automáticamente en cada PR del sistema de agentes.

---

## Archivos hub (más dependidos — tocar con cuidado)

- `app/main.py` — usado por 2 archivo(s): `tests/test_health.py`, `tests/test_students.py`
- `app/storage/memory_store.py` — usado por 2 archivo(s): `tests/test_students.py`, `app/routers/students.py`
- `app/models/student.py` — usado por 2 archivo(s): `app/routers/students.py`, `app/storage/memory_store.py`

---

## Entry points (sin dependencias internas)

- `app/models/student.py`
- `app/routers/__init__.py`

---

## Grafo completo (lista de adyacencia)

### `app/__init__.py`
- _(sin dependencias internas)_

### `app/main.py`
- → `app/routers/__init__.py`

### `app/models/__init__.py`
- _(sin dependencias internas)_

### `app/models/student.py`
- _(sin dependencias internas)_

### `app/routers/__init__.py`
- _(sin dependencias internas)_

### `app/routers/health.py`
- _(sin dependencias internas)_

### `app/routers/students.py`
- → `app/models/student.py`
- → `app/storage/memory_store.py`

### `app/storage/__init__.py`
- _(sin dependencias internas)_

### `app/storage/memory_store.py`
- → `app/models/student.py`

### `tests/__init__.py`
- _(sin dependencias internas)_

### `tests/test_health.py`
- → `app/main.py`

### `tests/test_students.py`
- → `app/main.py`
- → `app/storage/memory_store.py`

---

## Guía de búsqueda rápida

| Si modificas... | Revisa también... |
|---|---|
| `app/main.py` | `tests/test_health.py`, `tests/test_students.py` |
| `app/storage/memory_store.py` | `tests/test_students.py`, `app/routers/students.py` |
| `app/models/student.py` | `app/routers/students.py`, `app/storage/memory_store.py` |
