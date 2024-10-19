async def aiohttp_handler(request):
    return web.json_response({"message": f"Hello from Aiohttp!"})
