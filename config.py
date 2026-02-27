import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SECRET_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dave:root@localhost/ico801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False