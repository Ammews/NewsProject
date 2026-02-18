from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(root_path="/api", lifespan=lifespan)




posts = {
    1: {"Title": "Title Teste", "Description": "Description Teste"},
    2: {"Title": "Title Teste2", "Description": "Description Teste2"}
    }



@app.get("/posts/{id}")
def getPostById(id: int):
    if id not in posts:
        raise HTTPException(status_code=404,detail="Post Not Found")
    return posts.get(id)

@app.post("/posts")
def createPost(post: PostCreate) -> PostCreate:
    newPost = {"title": post.title,"content" : post.content}
    posts[max(posts.keys()) + 1] = newPost
    return newPost