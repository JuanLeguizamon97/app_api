from config.database import Base
from sqlalchemy import ForeignKey, Column, Integer, String, Float, Boolean, JSON 
from sqlalchemy.orm import relationship

class Order(Base):

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    business_id = Column(Integer, ForeignKey('business.id'), nullable=False)
    items = Column(JSON, nullable=False)  # Puede ser un JSON para almacenar los detalles de los artículos
    total_price = Column(Float, nullable=False)
    status = Column(String, default='pending') # pending,confirmed,delivered, cancelled
    paid_account = Column(Boolean, default=False)

    # Relación con la factura
    invoice = relationship("Invoice", uselist=False, back_populates="order")