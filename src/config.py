import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' +os.path.join(basedir, 'repository.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "chave_segura_secreta"