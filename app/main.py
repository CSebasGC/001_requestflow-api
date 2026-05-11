from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.users import router as users_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)

app.include_router(health_router)
app.include_router(users_router)