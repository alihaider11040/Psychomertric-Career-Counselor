from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    user_id: int
    title: str
    description: str
class Feed(BaseModel):

    posts: List[Post]

class FeedSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FeedSingleton, cls).__new__(cls)
            cls._instance.feed = Feed(posts=[])
        return cls._instance