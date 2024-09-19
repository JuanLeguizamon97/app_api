from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from config.database import get_db
from sqlalchemy.orm import Session
from models.user import User as UserModel
from middlewares.jwt_bearer import JWTBearer
from services.user import create_user, get_user, get_users, delete_user
from schemas.user import UserBase, UserCreate, UserResponse

user_router = APIRouter(
    prefix='/users',
    tags=['users'],
    dependencies=[Depends(JWTBearer())]
)

@user_router.post('/', response_model= UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user= create_user(db, user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail= str(e))
    
@user_router.get('/{user_id}', response_model= UserResponse, status_code=200)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='user not found')
    return user

@user_router.delete('/{user_id}', status_code=204)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    try:
        delete_user(db, user_id)
        return JSONResponse(status_code=204, content=None)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))