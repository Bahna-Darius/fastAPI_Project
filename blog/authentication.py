from fastapi import APIRouter, HTTPException, status, Depends
import schemas, database, models, tokenn
from sqlalchemy.orm import Session
from hashing import verify_password
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends((database.get_db))):
    user = db.query(models.Users).filter(models.Users.name == request.username).first()
    # passw = db.query(models.Users).filter(models.Users.password == request.password).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")

    #verify password
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")

    access_token =tokenn.create_access_token(
                    data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}


