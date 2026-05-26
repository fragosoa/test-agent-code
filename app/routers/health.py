"""Router para endpoints de health check y hello world."""

from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health", summary="Health check")
async def health_check() -> dict:
    """Verifica que la aplicación está corriendo correctamente."""
    return {"status": "ok", "message": "Service is healthy"}


@router.get("/hello", summary="Hello World")
async def hello_world() -> dict:
    """Endpoint básico de Hello World."""
    return {"message": "Hello, World!"}
