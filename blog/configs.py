class BaseConfig(object):
    WTF_CSRF_ENABLED = True
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '(&5l9r#ak545-zg7a(30b4ft!jomxe7z%7k)_(&u347k91=#h+'
    FLASK_ADMIN_SWATCH = 'cosmo'


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
