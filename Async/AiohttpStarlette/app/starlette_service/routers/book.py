from starlette.routing import Route

from app.config import get_logger
from app.pkg.common import BaseRouter
from app.pkg.common.schema import HttpVerbs
from app.pkg.repository.book import BookRepository
from app.pkg.schema import (
    GetBookByNameSchema,
    CreateBookSchema,
    DeleteBookByNameSchema,
    UpdateBookSchema,
)
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.endpoints import HTTPEndpoint

from app.pkg.utils import validate_request_starlette

logger = get_logger()


class BookRouter(HTTPEndpoint, BaseRouter):
    repository: BookRepository = BookRepository()

    @validate_request_starlette(schema=GetBookByNameSchema)
    async def get(self, request: Request, query: GetBookByNameSchema):
        result = await self.repository.get_by_name(query)
        if result is None:
            logger.error(f"404, book not found with name {query.name}")
            raise HTTPException(status_code=404, detail="Book not Found!")
        logger.info(f"Find book with name {query.name}!!")
        return JSONResponse(result.model_dump_json())

    @validate_request_starlette(schema=CreateBookSchema)
    async def post(self, request: Request, query=CreateBookSchema):
        result = await self.repository.create(cmd=query)
        if result is None:
            logger.error(f"Find same row in base, with name {query.name}")
            raise HTTPException(status_code=400, detail="Book already exist!")
        logger.info(f"Create Book {query}")
        return JSONResponse(result.model_dump_json())

    @validate_request_starlette(schema=DeleteBookByNameSchema)
    async def delete(self, request: Request, query: DeleteBookByNameSchema):
        result = await self.repository.delete_by_name(cmd=query)
        if result is None:
            logger.error(f"404, book not found with name {query.name}")
            raise HTTPException(status_code=404, detail="Book not found!")
        logger.info(f"Delete Book by name {query.name}")
        return JSONResponse(result.model_dump_json())

    @validate_request_starlette(schema=UpdateBookSchema)
    async def put(self, request: Request, query: UpdateBookSchema):
        result = await self.repository.update(cmd=query)
        if result is None:
            logger.error(f"404, book not found with name {query.old_name}")
            raise HTTPException(status_code=404, detail="Book not found!")
        logger.info(f"Update Book by name {query.name}")
        return JSONResponse(result.model_dump_json())

    @staticmethod
    def get_routers() -> Route:
        return Route(
            "/book",
            endpoint=BookRouter,
            methods=[
                HttpVerbs.GET.value,
                HttpVerbs.POST.value,
                HttpVerbs.PUT.value,
                HttpVerbs.DELETE.value,
            ],
        )
