import os

class BaseConfig(object):
    SECRET_KEY = os.environ.get('secret_key') or "my_precious"
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
