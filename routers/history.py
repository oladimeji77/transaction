from fastapi import Depends, status, HTTPException, Response, APIRouter
from typing import List
from hash import hasher
from sqlalchemy.orm import Session
from database import engine, get_db 
import schema, model
from .jwttoken import get_current_user

router = APIRouter(prefix="/api/history", tags=['History'])


@router.get("/")
def history_all(db: Session = Depends(get_db), current_user: schema.TranxGLDb = Depends(get_current_user)):
    all = db.query(model.TranxGLDb).all()
    return all



