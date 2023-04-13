"""
Project entrypoint
"""
from starlette.applications import Starlette

routes = []
app = Starlette(debug=True, routes=routes)
