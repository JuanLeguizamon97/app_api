from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base  # Base declarativa de SQLAlchemy

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

    restaurant = relationship("Restaurant", back_populates="items")