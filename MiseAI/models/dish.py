from sqlalchemy import Column, Integer, String, Float
from database import Base

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    category = Column(String, nullable=True)
