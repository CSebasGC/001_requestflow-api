from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/")
def read_root():
    return {
        "message": "RequestFlow API is running",
        "project": "Proyecto 001",
        "name": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "ok",
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "requestflow-api",
        "environment": settings.ENVIRONMENT,
    }