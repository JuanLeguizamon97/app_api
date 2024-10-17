from fastapi import FastAPI, Depends, Path, Query, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config.database import db_session
from middlewares.jwt_bearer import JWTBearer
from models.business import Business as BusinessModel
from services.business import create_business, get_business
from schemas.business import BusinessProfile

business_router = APIRouter(
    prefix="/business",
    tags=["business"],
    dependencies=[Depends(JWTBearer())]
)

@business_router.post("/", response_model=None, status_code=201) #Añadir un schema para la respuesta de la creación del usuario restaurante
def create_new_business(business: BusinessProfile, db: Session = Depends(db_session)): #Crear el esquema de creación del perfil de restuarante
    try:
        new_profile= create_business(db, business)
        return new_profile
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
#Pendiente crear los endpoints para modificar, obtener y eliminar restaurantes