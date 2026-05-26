# Dependency Graph

> Generado automáticamente por análisis estático de imports · 2026-05-26 UTC
> Una arista A → B significa 'A importa B'.
> Actualizado automáticamente en cada PR del sistema de agentes.

---

## Archivos hub (más dependidos — tocar con cuidado)

| Archivo | Dependido por |
|---|---|
| `app/models/student.py` | `app/storage/memory_store.py`, `app/routers/students.py` |
| `app/storage/memory_store.py` | `app/routers/students.py`, `tests/test_students.py` |
| `app/main.py` | `tests/test_health.py`, `tests/test_students.py` |

---

## Entry points (sin dependencias internas)

| Archivo | Descripción |
|---|---|
| `app/routers/health.py` | No importa módulos internos del proyecto |

---

## Grafo completo (lista de adyacencia)

```
app/main.py
  → app/routers/health.py
  → app/routers/students.py

app/routers/students.py
  → app/models/student.py
  → app/storage/memory_store.py

app/storage/memory_store.py
  → app/models/student.py

tests/test_health.py
  → app/main.py

tests/test_students.py
  → app/main.py
  → app/storage/memory_store.py
```

---

## Guía de búsqueda rápida

| Si modificas... | Revisa también... |
|---|---|
| `app/models/student.py` | `app/storage/memory_store.py`, `app/routers/students.py`, `tests/test_students.py` |
| `app/storage/memory_store.py` | `app/routers/students.py`, `tests/test_students.py` |
| `app/routers/health.py` | `tests/test_health.py` |
| `app/routers/students.py` | `tests/test_students.py` |
| `app/main.py` | `tests/test_health.py`, `tests/test_students.py` |
