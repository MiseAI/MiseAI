from database import engine
from models import user

user.Base.metadata.create_all(bind=engine)

print("✅ Database initialized.")
