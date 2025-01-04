from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    pg_name: str  # Ensure the names match the environment variables
    pg_host: str
    pg_port: str
    pg_user: str
    pg_password: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.pg_user}:{self.pg_password}@{self.pg_host}:{self.pg_port}/{self.pg_name}?sslmode=require"

    class Config:
        env_file = ".env"  # Specify the environment file to load
        extra = "ignore"  # Ignore extra fields in the .env file

