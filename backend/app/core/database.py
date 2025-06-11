from motor.motor_asyncio import AsyncIOMotorClient
from .config import Settings

settings = Settings()
client = AsyncIOMotorClient(settings.mongo_url)
db = client[settings.mongo_db]