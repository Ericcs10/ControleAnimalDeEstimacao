from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_HOST: str = "localhost"
    MONGO_PORT: int = 27017
    MONGO_USER: str = "root"
    MONGO_PASS: str = "example"
    MONGO_DB: str = "petdb"
    MONGODB_NAME: str = "petdb"  # 🔥 Adicionado

    @property
    def MONGODB_URL(self):
        return f"mongodb://{self.MONGO_USER}:{self.MONGO_PASS}@{self.MONGO_HOST}:{self.MONGO_PORT}"

    class Config:
        env_file = ".env.docker"


settings = Settings()
