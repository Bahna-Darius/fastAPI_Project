from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"data": {"message": "Hello World"}}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"data": {"message": f"Hello {name}"}}



