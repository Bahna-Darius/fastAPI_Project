from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"data": "blog list"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": {"message": "all unpublished blogs"}}


@app.get("/blog/{id}")      #fetch blog with id = id
async def show(id: int):
    return {"data": {"message": f"{id}"}}


@app.get("/blog/{id}/comments")     #fetch comments of blog with id = id
async def comments(id):
    return {"data": {"1", "2"}}

