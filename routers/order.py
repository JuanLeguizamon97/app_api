from fastapi import FastAPI, Depends, Path, Query, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config.database import get_db
from models.order import Order as OrderModel
from middlewares.jwt_bearer import JWTBearer
from services.order import create_order, get_order, get_orders, delete_order
from schemas.order import OrderCreate, OrderResponse

order_router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    dependencies=[Depends(JWTBearer())]  # Protección JWT en todas las rutas
)

# Crear una nueva orden
@order_router.post("/", response_model=OrderResponse, status_code=201)
def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        new_order = create_order(db, order)
        return new_order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Obtener una orden por su ID
@order_router.get("/{order_id}", response_model=OrderResponse)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

# Obtener todas las órdenes
@order_router.get("/", response_model=list[OrderResponse])
def read_orders(db: Session = Depends(get_db)):
    orders = get_orders(db)
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found")
    return orders

# Eliminar una orden por su ID
@order_router.delete("/{order_id}", status_code=204)
def delete_existing_order(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    try:
        delete_order(db, order_id)
        return JSONResponse(status_code=204, content=None)  # No content response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
