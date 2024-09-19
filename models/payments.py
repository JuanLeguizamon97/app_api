from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship

class Payment(Base):

    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)  # credit_card, debit_card, paypal, etc.
    payment_status = Column(String, default='pending')  # pending, completed, failed

    user = relationship("User")
    order = relationship("Order")