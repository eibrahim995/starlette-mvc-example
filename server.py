"""
Project entrypoint
"""
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.routing import Route

from utils.auth import BasicAuthBackend, on_auth_error
from views import posts_view

routes = [
    Route('/posts', endpoint=posts_view, methods=['GET']),
]
middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend(), on_error=on_auth_error)
]
app = Starlette(debug=True, routes=routes, middleware=middleware,)
