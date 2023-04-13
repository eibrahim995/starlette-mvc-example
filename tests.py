from starlette.testclient import TestClient

from models import Post
from server import app


def test_posts_endpoint():
    client = TestClient(app)
    client.headers = {"Authorization": "Basic aGVtYTpoZW1h"}  # username: hema, password: hema
    response = client.get('/posts')
    assert response.status_code == 200
    assert response.json().get("result") == Post.objects.select("user_id", 1)


def test_middleware_no_auth():
    client = TestClient(app)
    response = client.get('/posts')
    assert response.status_code == 403
    assert response.json().get("errors") == {"auth": "You are not authorized to view this resource"}


def test_middleware_wrong_auth():
    client = TestClient(app)
    client.headers = {"Authorization": "Basic aGVtYTE6aGVtYQ=="}  # username: hema1, password: hema
    response = client.get('/posts')
    assert response.status_code == 403
    assert response.json().get("errors") == {"auth": "You are not authorized to view this resource"}


# test_posts_endpoint()
# test_middleware_no_auth()
# test_middleware_wrong_auth()
