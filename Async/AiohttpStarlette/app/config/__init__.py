from app.config.logger import get_logger
from app.config.settings import Settings


__all__ = [
    "get_logger",
    "settings",
]

settings = Settings()
