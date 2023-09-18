from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()


#create new blog in db
@app.post("/blogv2", status_code=status.HTTP_201_CREATED) #status_code add
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()   #save modification
    db.refresh(new_blog)
    return new_blog


@app.delete("/blog/{id}")
def delete_blog(id, db: Session = Depends(get_db)):
    (db.query(models.Blog).filter(models.Blog.id ==
                                  id).delete(synchronize_session=False))
    db.commit()

    messaje = HTTPException(status_code=status.HTTP_200_OK,
                    detail=f"Blog with id:{id} has been successfully deleted")

    return {"data": messaje}


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog_id(request: schemas.Blog, id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():  #check the id is valid
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not fond!")
    else:
        # Convert the Pydantic model to a dictionary
        blog_data = dict(request)

        # Update the blog using the dictionary data
        blog.update(blog_data)

        db.commit()

    return {"data": "updated success"}


@app.get("/blog")
def all_blogs_return(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # if not blog:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"detail": f"Blog with the id {id} is not available"}

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")

    return blog


