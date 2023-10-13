from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVICE_NAME: str = 'Q&A_API'
    DB_HOST: str = '127.0.0.1'
    DB_PORT: int = 5432
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str = 'ques_and_ans_api'
   
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
