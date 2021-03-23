import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    UPLOAD_FOLDER = './app/static/uploads'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://yourusername:yourpassword@localhost/databasename'
    SQLALCHEMY_DATABASE_URI = 'postgresql://ilceufpmxwusmc:bce3d1f3ab50f108d8c028fee475096190a585d98ad7fb22543828825c0982e8@ec2-54-161-239-198.compute-1.amazonaws.com:5432/diubuogd6ksll'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False