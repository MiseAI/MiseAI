import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
Database
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True,  # Shows SQL queries in logs (good for debugging)
    future=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()