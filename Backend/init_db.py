from database import Base, engine
from models.user import User

print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Done.")
