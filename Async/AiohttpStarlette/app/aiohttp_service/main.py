from aiohttp import web

from app.aiohttp_service.router import get_routes
from app.config import settings
from app.pkg.common import BaseServer


class AioHttpServer(BaseServer):
    __app = web.Application()

    def _add_routes(self):
        self.__app.router.add_routes(
            get_routes(),
        )

    async def run(self):
        self._add_routes()
        runner = web.AppRunner(self.__app)
        await runner.setup()
        site = web.TCPSite(runner, settings.AIO_HOST, settings.AIO_PORT)
        await site.start()
