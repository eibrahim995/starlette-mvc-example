"""
Application Views
The view typically shouldn't contain any logic, it just fetches the data from the controller and formats it.
"""
from starlette.requests import Request
from starlette.responses import JSONResponse

from controllers import PostsController


def posts_view(request: Request) -> JSONResponse:
    controller = PostsController()
    data = controller.get_posts()
    return JSONResponse({"result": [item.dict() for item in data]})
