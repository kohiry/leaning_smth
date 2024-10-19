from aiohttp import web

from app.aiohttp_service.routers import BookRouter
from app.config import settings
from app.pkg.common import BaseServer, BaseRouter


class AioHttpServer(BaseServer):
    __app = web.Application()
    __routers: list[type[BaseRouter]] = [
        BookRouter,
    ]

    def _add_routes(self):
        self.__app.add_routes(*map(lambda router: router.get_routers(), self.__routers))

    async def run(self):
        self._add_routes()
        runner = web.AppRunner(self.__app)
        await runner.setup()
        site = web.TCPSite(runner, settings.AIO_HOST, settings.AIO_PORT)
        await site.start()
