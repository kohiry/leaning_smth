from app.base import BaseTransport
from app.config import get_logger


logger = get_logger()


class Car(BaseTransport):
    doors: int

    def __init__(
        self,
        mark: str,
        model: str,
        year_created: int,
        speed: int,
        doors: int,
    ):
        self.mark = mark
        self.model = model
        self.year_created = year_created
        self.speed = speed
        self.doors = doors

    def set_up(self):
        logger.info(f"Car {self.mark} {self.model} set up!")

    def stop(self):
        logger.info(f"Car {self.mark} {self.model} stop!")
