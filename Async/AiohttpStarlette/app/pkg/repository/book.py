from app.pkg.common import BaseRepository
from app.pkg.models import Book
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


class BookRepository(BaseRepository):
    @session_dependency
    async def get_by_name(
        self,
        query: GetBookByNameSchema,
        session: AsyncSession,
    ) -> BookSchema | None:
        result = await session.execute(select(Book).where(Book.name == query.name))
        book = result.scalar_one_or_none()
        if book is None:
            return None
        return BookSchema.model_validate(book)

    @session_dependency
    async def create(self, cmd: CreateBookSchema, session: AsyncSession):
        pass

    @session_dependency
    async def delete_by_name(self, cmd: DeleteBookByNameSchema, session: AsyncSession):
        pass

    @session_dependency
    async def update(self, cmd: UpdateBookSchema, session: AsyncSession):
        pass
