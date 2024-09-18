from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    resturant_id = Column(Integer) #Foreign key
    items = Column(dict)
    status = Column(Boolean)
    paid_account = Column(Boolean)    
    