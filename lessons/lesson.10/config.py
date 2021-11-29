import os


class BaseConfig:
    ENV = "development"
    DEBUG = False
    TESTING = False
    # sqla
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
    SECRET_KEY = "abc"
    #
    HOST = "127.0.0.1"
    PORT = 5000


class ProductionConfig(BaseConfig):
    ENV = "production"
    DEBUG = False
    TESTING = False
    HOST = "0.0.0.0"
    SECRET_KEY = os.getenv("SECRET_KEY", "sdfsgsrg")


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    DEBUG = True
    TESTING = False
    HOST = "0.0.0.0"


class TestingConfig(BaseConfig):
    DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True
    TESTING = True
