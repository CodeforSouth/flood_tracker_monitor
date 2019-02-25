import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY'] or 'dev'
    TWILIO_ACCOUNT_ID = os.environ['TWILIO_ACCOUNT_ID']
    TWILIO_SECRET_KEY = os.environ['TWILIO_SECRET_KEY']
    TWILIO_VERIFY_SECRET_KEY = os.environ['TWILIO_VERIFY_SECRET_KEY']
    PARTICLE_SECRET_KEY = os.environ['PARTICLE_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # CELERY_BROKER_URL = 'redis://redis:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://redis:6379/0'