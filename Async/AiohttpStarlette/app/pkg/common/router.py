from abc import ABCMeta, abstractmethod
from typing import Any

from app.pkg.common import BaseRepository


__all__ = [
    "BaseRouter",
]


class BaseRouter(metaclass=ABCMeta):
    repository: BaseRepository

    @abstractmethod
    async def get(self, request: Any):
        pass

    @abstractmethod
    async def post(self, request: Any):
        pass

    @abstractmethod
    async def delete(self, request: Any):
        pass

    @abstractmethod
    async def put(self, request: Any):
        pass

    @staticmethod
    @abstractmethod
    def get_routers() -> Any:
        pass
