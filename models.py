from database import Base
from sqlalchemy import Column,String,Boolean,Integer,Float

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, index = True)
    description = Column(String, index = True)
    price = Column(Float)
    is_available = Column(Boolean, default=True)
