from typing import Any

from aiohttp import web

from app.config import get_logger
from app.pkg.common import BaseRouter
from app.pkg.repository.book import BookRepository, logger
from app.pkg.schema import (
    GetBookByNameSchema,
    CreateBookSchema,
    DeleteBookByNameSchema,
    UpdateBookSchema,
)
from app.pkg.utils import validate_request_aiohttp

routes = web.RouteTableDef()
logger = get_logger()


@routes.view("/book")
class BookRouter(web.View, BaseRouter):
    repository: BookRepository = BookRepository()

    @validate_request_aiohttp(schema=GetBookByNameSchema)
    async def get(self, query: GetBookByNameSchema):
        logger.info(1111)
        return web.json_response({"Hello": "zxc"})

    async def post(self):
        return web.Response()

    async def delete(self):
        return web.Response()

    async def put(self):
        return web.Response()

    @staticmethod
    def get_routers() -> Any:
        return routes
