from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_core.core_schema import NoneSchema
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

class Bot(BaseModel):
    token: str

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    bot: Bot
    db: DatabaseConfig

settings = Settings()
