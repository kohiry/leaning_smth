from abc import ABCMeta, abstractmethod
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from app.pkg.repository.base import BaseRepository
from starlette.routing import Route


class BaseRouter(HTTPEndpoint, metaclass=ABCMeta):
    repository: BaseRepository

    @abstractmethod
    async def get(self, request: Request):
        pass

    @abstractmethod
    async def post(self, request: Request):
        pass

    @abstractmethod
    async def delete(self, request: Request):
        pass

    @abstractmethod
    async def put(self, request: Request):
        pass

    @staticmethod
    @abstractmethod
    def get_routers() -> Route:
        pass
