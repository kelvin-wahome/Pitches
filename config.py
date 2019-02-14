import os


class Config:
    SECRET_KEY = 'SECRET_KEY'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blackrose:callofduty6996@localhost/pitches'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'pitches'
    MAIL_USERNAME = os.environ.get("wahomekelving@gmail.com")
    MAIL_PASSWORD = os.environ.get("alisak6996")


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blackrose:callofduty6996@localhost/pitches'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
