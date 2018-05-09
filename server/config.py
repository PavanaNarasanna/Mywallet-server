import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'sEcReTKeY'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    PASSWORD_SCHEMES = ['pbkdf2_sha512']
    ROLE = "HCC Coder"


class AwsS3Config(object):
    ACCESS_KEY = os.environ['S3_ACCESS_KEY']
    SECRET_KEY = os.environ['S3_SECRET_KEY']
    BUCKET_NAME = 'lp02-team-s-pdf-storage'
