from typing import List
from fastapi import FastAPI, Depends, status, HTTPException, Response
import models, schemas, database, authentication
from database import engine, get_db
from sqlalchemy.orm import Session
from hashing import hash_password
from passlib.context import CryptContext
from oauth2 import get_current_user

app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)


#create new blog in db
@app.post("/blogv2", status_code=status.HTTP_201_CREATED, tags=["Blogs"]) #status_code add
def create_blog(request: schemas.Blog, db: Session = Depends(get_db),
                get_current_user: schemas.User = Depends(get_current_user)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()         #save modification
    db.refresh(new_blog)

    return new_blog


@app.delete("/blog/{id}", tags=["Blogs"])
def delete_blog(id, db: Session = Depends(get_db),
                get_current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found!")
    else:
        blog.delete(synchronize_session=False)
        db.commit()

    return {"data": "delete blog success"}


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
def update_blog_id(request: schemas.Blog, id, db: Session = Depends(get_db),
                   get_current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():            #check the id is valid
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not fond!")
    else:
        # Convert the Pydantic model to a dictionary
        blog_data = dict(request)

        # Update the blog using the dictionary data
        blog.update(blog_data)

        db.commit()

    return {"data": "updated success"}


@app.get("/blog", response_model=List[schemas.ShowBlog], tags=["Blogs"])
def all_blogs_return(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=["Blogs"])  #defined the response, now it will only return the title, body from the basemodel
def show_blog_id(id, response: Response, db: Session = Depends(get_db),
                 get_current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # if not blog:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"detail": f"Blog with the id {id} is not available"}

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")

    return blog




                                #Create User:

# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto") #password encryption




@app.post("/user", response_model=schemas.ShowUser, tags=["Users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # hashedPassword = pwd_cxt.hash(request.password)

    new_user = models.Users(name=request.name, email=request.email,
                            password=hash_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get("/user/{id}", response_model=schemas.ShowUser, tags=["Users"])
def get_user_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    return user

