from config.database import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Invoice(Base):

    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    total_price = Column(Float, nullable=False)
    taxes = Column(Float, nullable=False)
    total_with_taxes = Column(Float, nullable=False)

    # Relación con la orden
    order = relationship("Order", back_populates="invoice")
    
    # El acceso a los items se hace a través de la relación con la tabla de órdenes
    @property
    def items(self):
        return self.order.items  # Los items se extraen directamente de la orden asociada