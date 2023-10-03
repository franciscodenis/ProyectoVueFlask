class Config(object):
    """Base Configuration"""

    SECRET_KEY="secret"
    TESTING=False
    SESSION_TYPE="filesystem"

class ProductionConfig(Config):
    """Production Config"""
    pass

class DevelopmentConfig(Config):
    """Development Config"""
    DB_USER = "postgres"
    DB_PASS = "abc123"
    DB_HOST = "localhost"
    DB_NAME = "grupo32"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        F"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )

class TestingConfig(Config):
    """Testing Config"""
    TESTING=True
    pass

config = {
    "production" : ProductionConfig,
    "development" : DevelopmentConfig,
    "testing" : TestingConfig
    }

