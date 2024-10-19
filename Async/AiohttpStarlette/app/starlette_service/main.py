from starlette.applications import Starlette
import uvicorn

from app.base import BaseServer
from app.config import settings
from app.starlette_service.routers import BookRouter, BaseRouter


class StarletteServer(BaseServer):
    __app = Starlette()
    __routers: list[type[BaseRouter]] = [
        BookRouter,
    ]

    async def _add_routes(self):
        return self.__app.routes.append(
            *map(lambda router: router.get_routers(), self.__routers)
        )

    async def run(self):
        await self._add_routes()
        config = uvicorn.Config(
            self.__app,
            host=settings.STAR_HOST,
            port=settings.STAR_PORT,
            log_level=settings.LOG_LEVEL.lower(),
        )
        server = uvicorn.Server(config)
        await server.serve()
