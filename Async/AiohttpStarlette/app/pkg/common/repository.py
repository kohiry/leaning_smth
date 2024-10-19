from abc import ABCMeta, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from app.pkg.common import BaseSchema


__all__ = [
    "BaseRepository",
]


class BaseRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by_name(self, query: BaseSchema, session: AsyncSession) -> BaseSchema:
        pass

    @abstractmethod
    def create(self, cmd: BaseSchema, session: AsyncSession) -> BaseSchema:
        pass

    @abstractmethod
    def delete_by_name(self, cmd: BaseSchema, session: AsyncSession) -> BaseSchema:
        pass

    @abstractmethod
    def update(self, cmd: BaseSchema, session: AsyncSession) -> BaseSchema:
        pass
