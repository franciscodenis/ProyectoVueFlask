from os import environ


class Config(object):
    """Base configuration."""

    SECRET_KEY = "secret"
    TESTING = False
    SESSION_TYPE = "filesystem"

    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    DB_PORT = environ.get("DB_PORT", "5432")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        ##f"postgresql://postgres:abc123@localhost:5432/grupo32"
    )


class ProductionConfig(Config):
    """Production configuration."""

    pass


class DevelopmentConfig(Config):
    """Development configuration."""

    pass


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}
