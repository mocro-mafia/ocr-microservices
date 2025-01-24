from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    MONGO_INITDB_ROOT_USERNAME: str = os.getenv("MONGO_INITDB_ROOT_USERNAME", "")
    MONGO_INITDB_ROOT_PASSWORD: str = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "")
    MONGO_INITDB_DATABASE: str = os.getenv("MONGO_INITDB_DATABASE", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    ACCESS_TOKEN_EXPIRES_IN: int = int(os.getenv("ACCESS_TOKEN_EXPIRES_IN", 15))
    REFRESH_TOKEN_EXPIRES_IN: int = int(os.getenv("REFRESH_TOKEN_EXPIRES_IN", 60))
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    CLIENT_ORIGIN: str = os.getenv("CLIENT_ORIGIN", "")
    JWT_PRIVATE_KEY: str = os.getenv("JWT_PRIVATE_KEY", "")
    JWT_PUBLIC_KEY: str = os.getenv("JWT_PUBLIC_KEY", "")

settings = Settings()