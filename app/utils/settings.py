from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_url: str
    mongo_user: str
    mongo_password: str

    class Config:
        env_file = ".env"

settings = Settings()