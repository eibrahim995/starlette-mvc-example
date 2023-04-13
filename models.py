import json

from pydantic import BaseModel


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class FakeDB(metaclass=SingletonType):
    def __init__(self):
        self._raw_posts = json.load(open("posts.json"))

    def select(self, key, value):
        return [Post(**post) for post in self._raw_posts if post[key] == value]


class Post(BaseModel):
    post_id: int
    category_id: int
    user_id: int
    post_name: str
    post_title: str
    post_description: str


Post.objects = FakeDB()
