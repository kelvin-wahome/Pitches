import os

class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}
