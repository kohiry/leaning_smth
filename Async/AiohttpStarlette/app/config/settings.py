from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    STAR_HOST: str
    STAR_PORT: int
    AIO_HOST: str
    AIO_PORT: int
    LOG_LEVEL: str

    class Config:
        env_file = ".env"
