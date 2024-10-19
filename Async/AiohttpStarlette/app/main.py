import asyncio
from app.aiohttp_service import AioHttpServer
from app.starlette_service import StarletteServer


async def main():
    servers = [
        AioHttpServer(),
        StarletteServer(),
    ]
    await asyncio.gather(*map(lambda server: server.run(), servers))


if __name__ == "__main__":
    asyncio.run(main())

# TODO теперь мне нужно доделать все ручки startlette и перейти к роутингу aiohttp + не забыть сделать все в нужных пбстракциях
