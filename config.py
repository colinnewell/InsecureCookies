from os import environ


class Config(object):

    # generate with os.urandom(32)
    KEY = environ.get('ENCRYPTION_KEY') \
            or b'\x8ciVu`\xf1V\x05\xc0TQV\xf5-!\xdf\x833-0\xe2\x80\x98M\xa9\x838\x1f\xe4p/\xf9'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ.get('SECRET_KEY') \
        or ':\xfeV\x0b\xc2\xe4:[=pq~W\x8aP\xc8~\x1d~qZ!\x86\r'


class ProductionConfig(Config):
    # force keys to be provided rather
    # than using dev defaults.
    pass
    # FIXME: probably need to move this to another file
    # to prevent this from crashing everything.
    # KEY = environ['ENCRYPTION_KEY']
    # SECRET_KEY = environ['SECRET_KEY']


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
