from config.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    resturant_id = Column(Integer) #Foreign key
    