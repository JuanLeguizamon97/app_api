from config.database import Base
from sqlalchemy import Column, String, Integer, Boolean, Float

class Restaurant(Base):

    __tablename__ = 'restaurants'

    restaurant_id = Column(Integer, primary_key = True)
    display_name = Column(String)
    legal_name = Column(String)
    tax_id = Column(Integer)
    restaurant_email = Column(String)
    restaurant_password = Column(String)
    address = Column(String)