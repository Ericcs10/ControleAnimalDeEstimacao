from motor.motor_asyncio import AsyncIOMotorClient
from .config import Settings

settings = Settings()
client = AsyncIOMotorClient(settings.mongodb_url)
db = client[settings.mongodb_name]
