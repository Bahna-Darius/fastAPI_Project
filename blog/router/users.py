# import database, models, schemas
# from sqlalchemy.orm import Session
# from fastapi import APIRouter, Depends, status, HTTPException
# from hashing import Hash
#
#
# get_db = database.get_db()
#
# router = APIRouter()
#
#
#
# # from passlib.context import CryptContext
# # from blog import database
#
# #Create User:
#
# # pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto") #password encryption
#
#
# @router.post("/user", response_model=schemas.ShowUser, tags=["Users"])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     # hashedPassword = pwd_cxt.hash(request.password)
#
#     new_user = models.Users(name=request.name, email=request.email,
#                             password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#
#     return new_user
#
#
# @router.get("/user/{id}", response_model=schemas.ShowUser, tags=["Users"])
# def get_user_id(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.Users).filter(models.Users.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#
#     return user
#
