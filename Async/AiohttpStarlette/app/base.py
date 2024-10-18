from abc import ABCMeta, abstractmethod


__all__ = ["BaseServer"]


class BaseServer(metaclass=ABCMeta):
    __app: object

    @abstractmethod
    def _add_routes(self):
        pass

    @abstractmethod
    async def run(self):
        pass
