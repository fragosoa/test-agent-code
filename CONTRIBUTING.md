# Guía para Contribuir

¡Gracias por tu interés en contribuir a **Student Management API**! Esta guía te ayudará a configurar tu entorno y seguir las convenciones del proyecto.

## Requisitos Previos

- **Python 3.12+**
- **Git**

## Configuración del Entorno de Desarrollo

1. **Clona el repositorio:**

   ```bash
   git clone <url-del-repositorio>
   cd mi-repo-prueba-v3
   ```

2. **Crea un entorno virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
   ```

3. **Instala las dependencias de desarrollo:**

   ```bash
   pip install -r requirements-dev.txt
   ```

   Esto instalará tanto las dependencias de producción (`requirements.txt`) como las de testing (pytest, httpx).

4. **Verifica que todo funcione ejecutando los tests:**

   ```bash
   python -m pytest tests/ -v
   ```

## Flujo de Trabajo para Contribuciones

### 1. Crea un branch

Nunca trabajes directamente sobre `main`. Crea un branch descriptivo para tu cambio:

```bash
git checkout -b feat/descripcion-corta   # Para nuevas funcionalidades
git checkout -b fix/descripcion-corta    # Para correcciones de bugs
git checkout -b docs/descripcion-corta   # Para cambios de documentación
```

### 2. Realiza tus cambios

- Sigue la estructura existente del proyecto (ver sección [Estructura del Proyecto](#estructura-del-proyecto)).
- Asegúrate de que tu código sea compatible con **Python 3.12+** (usa `str | None` en lugar de `Optional[str]`).
- Usa **Pydantic v2** para modelos y validaciones.

### 3. Escribe tests

- Agrega tests en el directorio `tests/` para cualquier funcionalidad nueva o bug corregido.
- Usa `TestClient` de FastAPI para tests de endpoints.
- Asegúrate de que cada test sea independiente y limpie su estado (usa fixtures con `autouse=True` cuando sea necesario).

### 4. Ejecuta los tests

Antes de hacer commit, asegúrate de que **todos los tests pasen**:

```bash
python -m pytest tests/ -v
```

### 5. Haz commits atómicos

Usa el formato [Conventional Commits](https://www.conventionalcommits.org/) para los mensajes de commit:

```
tipo(alcance): descripción breve en inglés
```

**Tipos comunes:**

| Tipo       | Descripción                          |
|------------|--------------------------------------|
| `feat`     | Nueva funcionalidad                  |
| `fix`      | Corrección de bug                    |
| `docs`     | Cambios en documentación             |
| `test`     | Agregar o modificar tests            |
| `refactor` | Refactorización sin cambio funcional |
| `chore`    | Tareas de mantenimiento              |

**Ejemplos:**

```bash
git commit -m "feat(students): add email uniqueness validation"
git commit -m "fix(storage): handle missing student gracefully"
git commit -m "docs(readme): update endpoint table"
```

### 6. Abre un Pull Request

- Haz push de tu branch al repositorio remoto.
- Abre un Pull Request hacia `main`.
- Describe claramente qué cambia y por qué.
- Asegúrate de que los tests pasen en CI antes de solicitar revisión.

## Estructura del Proyecto

```
app/
├── main.py                 # Entry point FastAPI, registro de routers
├── models/
│   └── student.py          # Schemas Pydantic (Create, Update, Response)
├── routers/
│   ├── health.py           # GET /health, GET /hello
│   └── students.py         # CRUD endpoints para /students
└── storage/
    └── memory_store.py     # Almacenamiento en memoria (diccionario Python)

tests/
├── test_health.py          # Tests de health y hello world
└── test_students.py        # Tests CRUD de estudiantes
```

Al agregar nuevas funcionalidades, sigue este patrón:

- **Modelos** en `app/models/`
- **Endpoints** en `app/routers/` (registra el router en `app/main.py`)
- **Lógica de almacenamiento** en `app/storage/`
- **Tests** en `tests/`

## Convenciones de Código

- Usa **type hints** en todas las funciones y parámetros.
- Usa la sintaxis moderna de tipos de Python 3.12+ (`str | None` en lugar de `Optional[str]`).
- Mantén las funciones de los routers enfocadas y pequeñas.
- Documenta endpoints con docstrings (FastAPI las usa para generar la documentación automática).

## Reporte de Bugs

Si encuentras un bug, abre un issue incluyendo:

1. **Descripción** clara del problema.
2. **Pasos para reproducir** el error.
3. **Comportamiento esperado** vs. comportamiento actual.
4. **Entorno** (sistema operativo, versión de Python).

## ¿Preguntas?

Si tienes dudas sobre cómo contribuir, abre un issue con la etiqueta `question` y te ayudaremos.
