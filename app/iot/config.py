import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY'] or 'dev'
    TWILIO_ACCOUNT_ID = os.environ['TWILIO_ACCOUNT_ID'] or 'dev'
    TWILIO_SECRET_KEY = os.environ['TWILIO_SECRET_KEY'] or 'dev'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
