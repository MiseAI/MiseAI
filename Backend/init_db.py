
# backend/init_db.py

from backend.database import Base, engine
from backend.models import user  # Make sure all models are imported so their tables are registered

def init():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    init()

