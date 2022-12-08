from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://demouser:demopass@localhost:5432/blog",
)

SECRET_KEY = getenv(
    "SECRET_KEY",
    "477b09f3c51a5e498bae69b23",
)


class Config:
    TESTING = False
    DEBUG = False
    ENV = "development"
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
