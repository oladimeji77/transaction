############  this module is currently not being used  ################
############  It has been moved to jwttoken or simplicity #############

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .jwttoken import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")



async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)

    