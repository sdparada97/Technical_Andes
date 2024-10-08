import os
from enum import Enum
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

env_folder = Path(__file__).parent.parent
env_file = env_folder / f".env.{os.getenv('ENV', 'dev')}"

load_dotenv(env_file)


class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"


class BaseSettings:
    BASE_DIR = Path(__file__).parent.parent.parent
    DEBUG = os.getenv('DEBUG')
    API_PREFIX = os.getenv('API_PREFIX')
    PROJECT_NAME = os.getenv('PROJECT_NAME')
    VERSION = os.getenv('VERSION')
    DESCRIPTION = os.getenv('DESCRIPTION')
    DATABASE_URL = f"mongodb://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@mongo:{os.getenv('DATABASE_PORT')}"


class DevSettings(BaseSettings):
    MODE = ModeEnum.development
    DATABASE_URL = f"mongodb://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@mongo:{os.getenv('DATABASE_PORT')}"


class ProdSettings(BaseSettings):
    MODE = ModeEnum.production
    DATABASE_URL = f"mongodb://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@mongo:{os.getenv('DATABASE_PORT')}"


@lru_cache()
def get_settings():
    env = os.getenv("ENV", "dev").lower()
    if env == "dev":
        return DevSettings()
    elif env == "prod":
        return ProdSettings()
    else:
        raise ValueError(f"Unsupported environment: {env}")


settings = get_settings()
