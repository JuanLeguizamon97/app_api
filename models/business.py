from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class Business(Base):

    __tablename__ = "business"

    business_id = Column(Integer, primary_key=True)
    business_name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    legal_representative_name= Column(String, nullable=False)
    legal_representative_number = Column(Integer, unique=True, nullable=False)
    phone_number = Column(Integer,unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_restaurant = Column(Boolean, default= False)
    is_active = Column(Boolean, default=True)

    #Pendiente revisar como podemos obtener los datos de latitud y longitud del API de Google maps para geolocalización

    orders = relationship("Order", back_populates="user")