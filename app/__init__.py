from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)

migrate = Migrate(app,db)

Login_manager = LoginManager()
Login_manager.init_app(app)
Login_manager.login_view = 'login'

from app import views