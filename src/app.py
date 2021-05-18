from flask import Flask, app
from src.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #, MigrateCommand
from flask_login import LoginManager
#from flask_script import Manager

#Star the flask app
application = Flask(__name__)

# Configuration
application.config.from_object(Config())
#application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////repository.db'

db = SQLAlchemy(application)
migrate = Migrate(application, db)

#manager = Manager(application)
#manager.add_command("db", MigrateCommand)

loginManager = LoginManager()
loginManager.init_app(application)

from src.models import tables, forms
from src.controllers import hello, index