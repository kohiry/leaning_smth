from abc import ABCMeta, abstractmethod


__all__ = ["BaseServer"]

from app.pkg.common import BaseRouter


class BaseServer(metaclass=ABCMeta):
    __app: object
    __routers: list[BaseRouter]

    @abstractmethod
    def _add_routes(self):
        pass

    @abstractmethod
    async def run(self):
        pass
