from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_url: str
    mongodb_name: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
