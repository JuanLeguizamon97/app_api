from fastapi import FastAPI, Depends, Path, Query, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session
from models.order import Order as OrderModel
from middlewares. jwt_bearer import JWTBearer
from services.order import OrderService
from schemas.order import Order

order_router = APIRouter()

@order_router.get('/orders', tags=['orders'], response_model=List[OrderModel], status_code=200, dependencies=[Depends(JWTBearer())])
def get_orders() -> List[Order]:
    db = Session()
    result = OrderService(db).get_orders()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))