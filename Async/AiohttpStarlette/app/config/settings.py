from pydantic_settings import BaseSettings

__all__ = [
    "settings",
]


class Settings(BaseSettings):
    STAR_HOST: str
    STAR_PORT: int

    AIO_HOST: str
    AIO_PORT: int
    LOG_LEVEL: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DRIVER_ALEMBIC: str
    POSTGRES_DRIVER_SQLALCHEMY: str

    class Config:
        env_file = ".env"


settings = Settings()
