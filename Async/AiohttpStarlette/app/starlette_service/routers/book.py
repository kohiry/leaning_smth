from starlette.routing import Route

from app.config import get_logger
from app.pkg.common import BaseRouter
from app.pkg.common.schema import HttpVerbs
from app.pkg.repository.book import BookRepository
from app.pkg.schema import GetBookByNameSchema
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

    async def post(self, request: Request):
        pass

    async def delete(self, request: Request):
        pass

    async def put(self, request: Request):
        pass

    @staticmethod
    def get_routers() -> Route:
        return Route(
            "/book",
            endpoint=BookRouter,
            methods=[
                HttpVerbs.GET.value,
                HttpVerbs.PUT.value,
                HttpVerbs.POST.value,
                HttpVerbs.DELETE.value,
            ],
        )
