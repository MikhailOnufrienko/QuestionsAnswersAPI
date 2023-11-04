from pydantic_settings import BaseSettings

from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    SERVICE_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
   
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
