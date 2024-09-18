from fastapi import FastAPI, Depends, Path, Query, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from models.order import Order as OrderModel
from middlewares. jwt_bearer import JWTBearer
from services.order import create_order, get_order, get_orders, delete_order
from schemas.order import OrderCreate, OrderResponse
from config.database import get_db

order_router = APIRouter()

@order_router.post("/orders/", response_model=OrderResponse)
def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)

@order_router.get("/orders/{order_id}", response_model=OrderResponse)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@order_router.get("/orders/", response_model=list[OrderResponse])
def read_orders(db: Session = Depends(get_db)):
    return get_orders(db)

@order_router.delete("/orders/{order_id}")
def delete_existing_order(order_id: int, db: Session = Depends(get_db)):
    delete_order(db, order_id)
    return {"msg": "Order deleted"}