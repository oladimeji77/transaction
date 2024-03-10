from fastapi import Depends, status, HTTPException, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from hash import hasher, verify_password
from sqlalchemy.orm import Session
from database import get_db 
import model
from .jwttoken import create_access_token

router = APIRouter(prefix="/api/auth", tags=['Auth'])

@router.post("/login")
def Login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    passwd = hasher(request.password)
    user = db.query(model.UserDB).filter(model.UserDB.Email == request.username).first()
    if not user:  #only if not works, == None doesn't
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Username or Password is incorrect")
    if not verify_password(request.password, user.Password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Username or Password is incorrect")
    
    access_token = create_access_token(data={"sub": user.Email})
    return {"access_token":access_token, "token_type":"bearer"}








 


