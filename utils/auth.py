import base64
import binascii

from starlette.authentication import AuthenticationBackend, AuthenticationError, AuthCredentials, SimpleUser
from starlette.requests import Request
from starlette.responses import JSONResponse


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        if "Authorization" not in conn.headers:
            raise AuthenticationError("No auth provided")

        auth = conn.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        if username == "hema" and password == "hema":
            return AuthCredentials(["authenticated"]), SimpleUser("hema")
        else:
            raise AuthenticationError('Invalid basic auth credentials')


def on_auth_error(request: Request, exc: Exception):
    return JSONResponse({"errors": {"auth": "You are not authorized to view this resource"}}, status_code=403)