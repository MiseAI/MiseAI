from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    dish_id = Column(Integer, ForeignKey("dishes.id"), nullable=False)
    date = Column(Date, nullable=False)
    quantity_sold = Column(Integer, nullable=False)
