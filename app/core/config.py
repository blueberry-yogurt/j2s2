from pydantic import BaseModel
import os


class Settings(BaseModel):
    APP_NAME: str = os.getenv("APP_NAME", "J2S2 Diary API")
    API_V1_PREFIX: str = os.getenv("API_V1_PREFIX", "/api/v1")


settings = Settings()