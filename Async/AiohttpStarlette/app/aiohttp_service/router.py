from aiohttp import web


async def aiohttp_handler(request):
    return web.json_response({"message": f"Hello from Aiohttp!"})


def get_routes():
    return [
        web.get("/", handler=aiohttp_handler),
    ]
