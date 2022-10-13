from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path


class Settings(BaseSettings):
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/ervamate'
    DBBaseModel = declarative_base()
    TEMPLATES = Jinja2Templates(directory='templates')
    MEDIA = Path('media')
    AUTH_COOKIE_NAME: str = 'ervamate'
    SALTY: str = 'qC0dGhrekE-5BQbjkj5vqAi5CpfpEusGODzLUNfQbGnrVHugBAvKhxlX701pp5ir5DKuRAi92je_VLpTPMRhaQ'


     
    # >>> import secrets
    # >>> secrets.token_urlsafe(64)
    # 'qC0dGhrekE-5BQbjkj5vqAi5CpfpEusGODzLUNfQbGnrVHugBAvKhxlX701pp5ir5DKuRAi92je_VLpTPMRhaQ'

    class Config:
        case_sensitive = True



settings: Settings = Settings()
