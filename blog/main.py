from fastapi import FastAPI
import schemas, models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post("/blogv2")
def create(request: schemas.Blog):
    return request
