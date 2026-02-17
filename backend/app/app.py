from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate
app = FastAPI(root_path="/api")

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
    posts[max(posts.keys()) + 1] = {"title": post.title,"content" : post.content}