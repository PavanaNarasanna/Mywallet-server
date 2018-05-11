import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'sEcReTKeY'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    PASSWORD_SCHEMES = ['pbkdf2_sha512']
    ROLE = "HCC Coder"

