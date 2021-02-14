import os

from pathlib import Path
from dotenv import load_dotenv

# Load the dotenv config
HERE = Path(__file__).parent
env_path = HERE / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "DEFAULT_KEY")
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", "DEFAULT_SALT")
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    # Database
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "spamnet")
    DATABASE_USER = os.getenv("DATABASE_USER", "root")
    DATABASE_PASS = os.getenv("DATABASE_PASSWORD", "")
    MYSQL_URI = f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = MYSQL_URI

class TestingConfig(Config):
    Testing = True

class DevConfig(Config):
    pass

class ProductionConfig(Config):
    PRESERVE_CONTEXT_ON_EXCEPTION = True

ENV_CONFIG_DICT = dict(
    development=DevConfig, testing=TestingConfig, production=ProductionConfig
)

def get_config(config_name):
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)
