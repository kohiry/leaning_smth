from app.base import LogMetaClass
from app.config import get_logger


class Zxc(metaclass=LogMetaClass):
    logger = get_logger()

    def hello(self):
        self.logger.info(f"Hello World!")

    def bye(self):
        self.logger.info("Bye World :(")
