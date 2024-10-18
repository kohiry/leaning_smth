from app.base import BaseTransport
from app.config import get_logger
from app.interface import Motor

logger = get_logger()


class Plane(BaseTransport, Motor):
    max_height: float
    __fuel: int = 0

    def __init__(
        self, mark: str, model: str, year_created: int, speed: int, max_height: float
    ):
        self.mark = mark
        self.model = model
        self.year_created = year_created
        self.speed = speed
        self.max_height = max_height

    def set_up(self):
        logger.info(
            f"Plane {self.mark} {self.model} fly, with max height {self.max_height}"
        )
        self.refill(50)

    def refill(self, fuel):
        self.__fuel = fuel
        logger.info(f"Plane now with fuel {self.__fuel}")

    def stop(self):
        logger.info(f"Plane {self.mark} {self.model} stop!")
