# from typing import List
# from fastapi import APIRouter, Depends, status, HTTPException, Response
# from sqlalchemy.orm import Session
# import database, models, schemas
#
# router = APIRouter()
#
#
#                         #response_model = customizing the response for the API
# @router.get("/blog", response_model=List[schemas.ShowBlog], tags=["Blogs"])
# def all_blogs_return(db: Session = Depends(database.get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs
#
#
# #create new blog in db
# @router.post("/blogv2", status_code=status.HTTP_201_CREATED, tags=["Blogs"]) #status_code add
# def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()             #save modification
#     db.refresh(new_blog)
#     return new_blog
#
#
#                                     #tags = arranging by category API
# @router.delete("/blog/{id}", tags=["Blogs"])
# def delete_blog(id, db: Session = Depends(database.get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#
#     if not blog.first():    #statu-code = It is an error in the http code
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found!")
#     else:
#         blog.delete(synchronize_session=False)
#         db.commit()
#
#     return {"data": "delete blog success"}
#
#
# @router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
# def update_blog_id(request: schemas.Blog, id, db: Session = Depends(
#     database.get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():  #check the id is valid
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not fond!")
#     else:
#         # Convert the Pydantic model to a dictionary
#         blog_data = dict(request)
#
#         # Update the blog using the dictionary data
#         blog.update(blog_data)
#
#         db.commit()
#
#     return {"data": "updated success"}
#
#
# @router.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=["Blogs"])  #defined the response, now it will only return the title, body from the basemodel
# def show_blog_id(id, response: Response, db: Session = Depends(database.get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#
#     # if not blog:
#     #     response.status_code = status.HTTP_404_NOT_FOUND
#     #     return {"detail": f"Blog with the id {id} is not available"}
#
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id {id} is not available")
#
#     return blog
#
