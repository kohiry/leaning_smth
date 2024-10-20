import os

from app.config import get_logger

logger = get_logger()


def clear_console():
    """Очистить консоль."""
    os.system("clear")


def cat_file(filename: str):
    """Прочитать файл."""
    logger.info("Code Example:\n\n")
    os.system(f"vim -R app/data_structures/examples/{filename}")
