from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from .config import Config
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)
csrf = CSRFProtect(app)

app.config.from_object(Config)


db = SQLAlchemy()

migrate = Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views