from starlette.routing import Route

from app.config import get_logger
from app.pkg.repository.book import BookRepository
from app.pkg.schema import GetBookByNameSchema, HttpVerbs
from app.starlette_service.routers.base import BaseRouter
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException


logger = get_logger()


class BookRouter(BaseRouter):
    repository: BookRepository = BookRepository()

    async def get(self, request: Request):
        result = await self.repository.get_by_name(GetBookByNameSchema(name="zxc"))
        if result is None:
            logger.error("404, book not found with name=zxc")
            raise HTTPException(status_code=404, detail="Book not Found!")
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
