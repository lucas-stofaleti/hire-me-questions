from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_url: str
    mongo_user: str
    mongo_password: str
    
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()