from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Настройки Redis (Docker)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # Имя ленты сообщений
    STREAM_NAME: str = "signal:commands"

    # Флаг для демона (использовать ли веб-управление)
    USE_WEB_CONTROL: bool = True

    class Config:
        # Позволяет подгружать настройки из файла .env, если он есть
        env_file = ".env"


settings = Settings()