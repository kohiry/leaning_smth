from app.config import get_logger
from app.pkg.common import BaseRepository
from app.pkg.models import BookModel
from app.pkg.schema import (
    GetBookByNameSchema,
    BookSchema,
    CreateBookSchema,
    DeleteBookByNameSchema,
    UpdateBookSchema,
)
from app.pkg.utils import session_dependency
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update

logger = get_logger()

__all__ = [
    "BookRepository",
]


class BookRepository(BaseRepository):
    @session_dependency
    async def get_by_name(
        self,
        query: GetBookByNameSchema,
        session: AsyncSession,
    ) -> BookSchema | None:
        result = await session.execute(
            select(BookModel).where(BookModel.name == query.name)
        )
        book = result.scalar_one_or_none()
        if book is None:
            return None
        return BookSchema.model_validate(book)

    @session_dependency
    async def create(
        self, cmd: CreateBookSchema, session: AsyncSession
    ) -> BookSchema | None:
        result_check = await self.get_by_name(cmd)
        if result_check is not None:
            return None
        model = BookModel(**dict(cmd))
        session.add(model)
        await session.commit()
        return BookSchema.model_validate(model)

    @session_dependency
    async def delete_by_name(
        self,
        cmd: DeleteBookByNameSchema,
        session: AsyncSession,
    ) -> DeleteBookByNameSchema | None:
        result_check = await self.get_by_name(cmd)
        if result_check is None:
            return None
        result = delete(BookModel).where(BookModel.name == cmd.name)
        await session.execute(result)
        await session.commit()
        return cmd

    @session_dependency
    async def update(
        self,
        cmd: UpdateBookSchema,
        session: AsyncSession,
    ) -> BookSchema | None:
        result_check = await self.get_by_name(GetBookByNameSchema(name=cmd.old_name))
        if result_check is None:
            return None
        stmt = (
            update(BookModel)
            .where(BookModel.name == cmd.old_name)
            .values(name=cmd.name, author=cmd.author)
        )
        await session.execute(stmt)
        await session.commit()
        return BookSchema.model_validate(cmd)
