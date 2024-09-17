from models.order import Order as OrderModel
from schemas.order import Order

class OrderService():

    def __init__(self, db) -> None:
        self.db = db

    def get_orders(self, id):
        result = self.db.query(OrderModel).filter(OrderModel.id == id).all()
        return result
    
    def create_movie(self, order: Order):
        new_order = OrderModel(**order.model_dump())
        self.db.add(new_order)
        self.db.commit()

    def update_order(self, id:int, data: Order):
        order =self.db.query(OrderModel).filter(OrderModel.id == id).first()
        ##Methods to update orders

    def cancel_order(self, id:int):
        self.db.query(OrderModel).filter(OrderModel.id == id).delete()
        self.db.commit()