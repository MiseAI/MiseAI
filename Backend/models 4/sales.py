from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class SalesData(Base):
    __tablename__ = "sales_data"
    id = Column(Integer, primary_key=True)
