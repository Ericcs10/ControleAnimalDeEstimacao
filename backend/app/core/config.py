from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    mongodb_url: str
    mongodb_name: str

    class Config:
        env_file = ".env.test" if os.getenv("PYTHON_ENV") == "test" else ".env"
        env_file_encoding = "utf-8"


settings = Settings()
