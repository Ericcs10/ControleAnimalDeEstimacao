from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongodb_url: str = "mongodb://root:example@mongo:27017"
    mongodb_name: str = "petdb"
