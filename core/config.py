import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Stock Market"
    PROJECT_VERSION: str = "1.0.0"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    REDIS_URL: str = os.getenv("REDIS_URL")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins

    API_KEY = os.getenv("API_KEY")
    DB_URL = os.getenv("DB_URL")

    TEST_USER_EMAIL = "test@example.com"


settings = Settings()