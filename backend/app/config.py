import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    dynamodb_url: str = os.getenv("DYNAMODB_URL", "")
    aws_region: str = os.getenv("AWS_REGION", "eu-central-1")
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID", "test")
    aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY", "test")

settings = Settings()
