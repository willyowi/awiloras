from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
login_manager = LoginManger()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
Bootstrap=Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[confg_name])


    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)