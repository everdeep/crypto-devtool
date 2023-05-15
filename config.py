import os
from dotenv import load_dotenv

load_dotenv()


# Flask config class
class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_PROD")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


if os.environ.get("ENV") == "production":
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()
