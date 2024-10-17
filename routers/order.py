from fastapi import FastAPI, Depends, Path, Query, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config.database import db_session
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
def create_new_order(order: OrderCreate, db: Session = Depends(db_session)):
    try:
        new_order = create_order(db, order)
        return new_order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Obtener una orden por su ID
@order_router.get("/{order_id}", response_model=OrderResponse)
def read_order(order_id: int, db: Session = Depends(db_session)):
    db_order = get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

# Obtener todas las órdenes
@order_router.get("/", response_model=list[OrderResponse])
def read_orders(db: Session = Depends(db_session)):
    orders = get_orders(db)
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found")
    return orders

@order_router.get("/pending/{restaurant_id}", response_model=list[OrderResponse])
def get_pending_orders(restaurant_id: int, db: Session = Depends(db_session)):
    # Filtrar órdenes pendientes del restaurante por `restaurant_id` y `status=False` (pendiente)
    pending_orders = db.query(OrderModel).filter(
        OrderModel.restaurant_id == restaurant_id,
        OrderModel.status == False  # False indica que la orden está pendiente
    ).all()
    
    if not pending_orders:
        raise HTTPException(status_code=404, detail="No pending orders found for this restaurant")
    
    return pending_orders

# Eliminar una orden por su ID
@order_router.delete("/{order_id}", status_code=204)
def delete_existing_order(order_id: int, db: Session = Depends(db_session)):
    db_order = get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    try:
        delete_order(db, order_id)
        return JSONResponse(status_code=204, content=None)  # No content response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
