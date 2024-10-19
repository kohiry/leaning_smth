from aiohttp import web
from aiohttp.web_exceptions import HTTPNotFound, HTTPBadRequest

from app.config import get_logger
from app.pkg.common import BaseRouter
from app.pkg.repository.book import BookRepository
from app.pkg.schema import (
    GetBookByNameSchema,
    CreateBookSchema,
    DeleteBookByNameSchema,
    UpdateBookSchema,
)
from app.pkg.utils import validate_request_aiohttp

__all__ = [
    "AiohttpBookRouter",
]

routes = web.RouteTableDef()
logger = get_logger()


@routes.view("/book")
class AiohttpBookRouter(web.View, BaseRouter):
    repository: BookRepository = BookRepository()

    @validate_request_aiohttp(schema=GetBookByNameSchema)
    async def get(self, query: GetBookByNameSchema):
        result = await self.repository.get_by_name(query)
        if result is None:
            logger.error(f"404, book not found with name {query.name}")
            raise HTTPNotFound(text="Book not Found!")
        logger.info(f"Find book with name {query.name}!!")
        return web.json_response(result.model_dump_json())

    @validate_request_aiohttp(schema=CreateBookSchema)
    async def post(self, query: CreateBookSchema):
        result = await self.repository.create(cmd=query)
        if result is None:
            logger.error(f"Find same row in base, with name {query.name}")
            raise HTTPBadRequest(text="Book already exist!")
        logger.info(f"Create Book {query}")
        return web.json_response(result.model_dump_json())

    @validate_request_aiohttp(schema=DeleteBookByNameSchema)
    async def delete(self, query: DeleteBookByNameSchema):
        result = await self.repository.delete_by_name(cmd=query)
        if result is None:
            logger.error(f"404, book not found with name {query.name}")
            raise HTTPNotFound(text="Book not found!")
        logger.info(f"Delete Book by name {query.name}")
        return web.json_response(result.model_dump_json())

    @validate_request_aiohttp(schema=UpdateBookSchema)
    async def put(self, query: UpdateBookSchema):
        result = await self.repository.update(cmd=query)
        if result is None:
            logger.error(f"404, book not found with name {query.old_name}")
            raise HTTPNotFound(text="Book not found!")
        logger.info(f"Update Book by name {query.name}")
        return web.json_response(result.model_dump_json())

    @staticmethod
    def get_routers() -> web.RouteTableDef:
        return routes
