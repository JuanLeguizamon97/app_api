from sqlalchemy.orm import Session
from models.order import Order
from schemas.order import OrderCreate

def create_order(db: Session, order: OrderCreate):
    db_order = Order(
        restaurant_id=order.restaurant_id,
        items=order.items,
        total_price=order.total_price
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def get_orders(db: Session):
    return db.query(Order).all()

def delete_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()