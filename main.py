from fastapi import FastAPI
from typing import Optional
from body_request import Blog


app = FastAPI()


@app.get("/blog")
async def root(limit=10, published: bool = True, sort: Optional[str] = None):
    #only get 10 published blogs
    if published:
        return {"data": f"{limit} published blogs from the DB"}
    else:
        return {"data": f"{limit} blogs from the DB"}


@app.get("/blog/unpublished")
async def unpublished():
    return {"data": {"message": "all unpublished blogs"}}


@app.get("/blog/{id}")      #fetch blog with id = id
async def show(id: int):
    return {"data": {"message": f"{id}"}}


@app.get("/blog/{id}/comments")     #fetch comments of blog with id = id
async def comments(id):
    return {"data": {"1", "2"}}


@app.post("/blog")
async def create_blog(request: Blog):
    return {"data": f"Blog is created with title as {request.title}"}