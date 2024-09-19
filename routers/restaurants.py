from fastapi import FastAPI, Depends, Path, Query, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config.database import get_db
from middlewares.jwt_bearer import JWTBearer
from models.restaurant import Restaurants as RestaurantModel
from services.restaurant import create_restaurant, get_restaurants
from schemas.restaurant import RestaurantProfile

restaurant_router = APIRouter(
    prefix="/resturant",
    tags=["restaurant"],
    dependencies=[Depends(JWTBearer())]
)

@restaurant_router.post("/", response_model=RestaurantModel, status_code=201) #Añadir un schema para la respuesta de la creación del usuario restaurante
def create_new_restaurant(restaurant: RestaurantProfile, db: Session = Depends(get_db)): #Crear el esquema de creación del perfil de restuarante
    try:
        new_profile= create_restaurant(db, restaurant)
        return new_profile
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
#Pendiente crear los endpoints para modificar, obtener y eliminar restaurantes