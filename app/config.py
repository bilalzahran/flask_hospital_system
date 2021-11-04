import os
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL
class Config:
    def __init__(self):
        load_dotenv()
        self.DB_HOST: str = os.getenv("DB_HOST")
        self.DB_NAME: str = os.getenv("DB_NAME")
        self.DB_USER: str = os.getenv("DB_USER")
        self.DB_PASSWORD: str = os.getenv("DB_PASSWORD")
        self.DB_PORT: str = os.getenv("DB_PORT")
        self.DB_DRIVER: str = os.getenv("DB_DRIVER")
        self.JWT_KEY: str = os.getenv("JWT_KEY")
        self.JWT_HOUR: str = os.getenv("JWT_HOUR")


config = Config()

db_url = URL(
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME,
    drivername=config.DB_DRIVER
)