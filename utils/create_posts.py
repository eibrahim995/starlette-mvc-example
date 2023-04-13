import json
import random
from pydantic import BaseModel

class Post(BaseModel):
    post_id: int
    category_id: int
    user_id: int
    post_name: str
    post_title: str
    post_description: str


def generate_dummy_posts(num_posts):
    posts = []
    for i in range(num_posts):
        post = Post(
            post_id=i + 1,
            category_id=random.randint(1, 5),
            user_id=random.randint(1, 10),
            post_name=f"post_{i+1}",
            post_title=f"Post Title {i+1}",
            post_description=f"This is a dummy post description for post {i+1}."
        )
        posts.append(post.dict())
    return posts

dummy_posts = generate_dummy_posts(40)
print(json.dumps(dummy_posts))
