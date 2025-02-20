from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DB_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_SECONDS: int = 3600
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS:bool = False
    MAIL_SSL_TLS:bool = True
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    CLOUDINARY_NAME: str
    CLOUDINARY_API_KEY: int 
    CLOUDINARY_API_SECRET: str 

    TEMPLATE_FOLDER: Path = Path(__file__).parent.parent / 'services' / 'templates'
    model_config = ConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )

settings = Settings()
