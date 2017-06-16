from os import environ


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ.get('SECRET_KEY') \
        or ':\xfeV\x0b\xc2\xe4:[=pq~W\x8aP\xc8~\x1d~qZ!\x86\r'


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
