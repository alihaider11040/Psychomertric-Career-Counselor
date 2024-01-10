from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PostCreate(BaseModel):
    description: str
    email: str

class Post(PostCreate):
    id: int

# In-memory storage for posts (replace with a database in a real application)
posts_db = []
post_id_counter = 1

@app.post("/posts/", response_model=Post)
def create_post(post_create: PostCreate):
    global post_id_counter
    post = Post(id=post_id_counter, **post_create.dict())
    post_id_counter += 1
    posts_db.append(post)
    return post

@app.get("/posts/", response_model=List[Post])
def get_all_posts():
    return posts_db
