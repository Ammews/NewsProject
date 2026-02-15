from fastapi import FastAPI, HTTPException

app = FastAPI()

posts = {
    1: {"Title": "Title Teste", "Description": "Description Teste"},
    2: {"Title": "Title Teste2", "Description": "Description Teste2"}
    }

@app.get("/posts/{id}")
def getPostById(id: int):
    if id not in posts:
        raise HTTPException(status_code=404,detail="Post Not Found")
    return posts.get(id)