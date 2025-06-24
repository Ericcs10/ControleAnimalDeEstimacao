from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_HOST: str = "mongo"
    MONGO_PORT: int = 27017
    MONGO_USER: str = "root"
    MONGO_PASS: str = "example"
    MONGO_DB: str = "petdb" 

    @property
    def MONGODB_URL(self) -> str:
        return f"mongodb://{self.MONGO_USER}:{self.MONGO_PASS}@{self.MONGO_HOST}:{self.MONGO_PORT}/{self.MONGO_DB}?authSource=admin"

    class Config:
        env_file = ".env.docker"


settings = Settings()
