from starlette.applications import Starlette
import uvicorn

from app.base import BaseServer
from app.config import settings
from app.starlette_service.router import get_routes


class StarletteServer(BaseServer):
    __app = Starlette()

    def _add_routes(self):
        self.__app.routes.append(
            *get_routes(),
        )

    async def run(self):
        self._add_routes()
        config = uvicorn.Config(
            self.__app,
            host=settings.STAR_HOST,
            port=settings.STAR_PORT,
            log_level=settings.LOG_LEVEL,
        )
        server = uvicorn.Server(config)
        await server.serve()
