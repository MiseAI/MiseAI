
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
JWT_SECRET = os.getenv("JWT_SECRET", "super-secret-key")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
