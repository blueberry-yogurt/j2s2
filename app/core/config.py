from functools import lru_cache
from typing import Any, Dict

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Database
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = "j2s2Root!"
    DB_NAME: str = "j2s2"

    # App
    APP_NAME: str = "J2S2 API"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"

    #  JWT 설정 (추가)
    JWT_SECRET_KEY: str = "CHANGE_ME_SUPER_SECRET"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Tortoise ORM
    @property
    def DATABASE_URL(self) -> str:
        pw = self.DB_PASSWORD or ""
        return (
            f"mysql://{self.DB_USER}:{pw}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    @property
    def TORTOISE_ORM(self) -> Dict[str, Any]:
        return {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.mysql",
                    "credentials": {
                        "host": self.DB_HOST,
                        "port": self.DB_PORT,
                        "user": self.DB_USER,
                        "password": self.DB_PASSWORD,
                        "database": self.DB_NAME,
                        "charset": "utf8mb4",
                    },
                }
            },
            "apps": {
                "models": {
                    "models": [
                        "app.models",
                        "aerich.models",
                    ],
                    "default_connection": "default",
                }
            },
            "use_tz": False,
            "timezone": "Asia/Seoul",
        }

    # pydantic-settings v2
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
