import os
basedir = os.path.asbpath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']