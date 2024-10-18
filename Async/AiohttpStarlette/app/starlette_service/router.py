from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.routing import Mount


async def starlette_homepage(request):
    return JSONResponse({"message": f"Hello from Starlette!"})


def get_routes():
    # return Mount(
    #         '/zxc',  # should start with /
    #         routes=[
    #             Route('/', starlette_homepage, methods=["GET"]),
    #         ]
    #     )
    return [
        Route("/", starlette_homepage, methods=["GET"]),
    ]
