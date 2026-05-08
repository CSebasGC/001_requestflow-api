from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "RequestFlow API"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "API backend para la gestión de solicitudes institucionales y empresariales"
    ENVIRONMENT: str = "development"
    
    DATABASE_URL: str = "postgresql+psycopg://postgres:postgres@localhost:5432/requestflow_db"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        )
    
    
settings = Settings()