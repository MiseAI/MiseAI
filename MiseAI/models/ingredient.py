from sqlalchemy import Column, Integer, String, Float
from database import Base

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    unit = Column(String, nullable=False)
    latest_price = Column(Float, nullable=True)
