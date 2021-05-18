
class Config:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////repository.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "chave_segura_secreta"