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
    pass

class TestingConfig(Config):
    """Testing Config"""
    TESTING=True
    pass

config = {
    "production" : ProductionConfig,
    "development" : DevelopmentConfig,
    "testing" : TestingConfig
    }

