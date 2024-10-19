from abc import ABCMeta, abstractmethod


__all__ = ["BaseServer"]

# from app.starlette_service.routers import BaseRouter
# TODO тут проблема циркулярного импорта, так как ты не сделал базовую абстракцию роутинга выше starlette библотеки


class BaseServer(metaclass=ABCMeta):
    __app: object
    __routers: list

    @abstractmethod
    def _add_routes(self):
        pass

    @abstractmethod
    async def run(self):
        pass
