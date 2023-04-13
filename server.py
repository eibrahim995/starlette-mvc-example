"""
Project entrypoint
"""
from starlette.applications import Starlette
from starlette.routing import Route

from views import posts_view

routes = [
    Route('/posts', endpoint=posts_view, methods=['GET']),
]

app = Starlette(debug=True, routes=routes)
