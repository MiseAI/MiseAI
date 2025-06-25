
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class SalesData(Base):
    __tablename__ = "sales_data"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    quantity_sold = Column(Integer)
    revenue = Column(Float)
    cost = Column(Float)
    date = Column(Date)

    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    restaurant = relationship("Restaurant", back_populates="sales")
