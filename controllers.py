"""
Application Controllers
"""
from models import Post


class PostsController:
    def get_posts(self):
        return Post.objects.select("user_id", 1)
