from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mongodb_url: str
    mongodb_name: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
