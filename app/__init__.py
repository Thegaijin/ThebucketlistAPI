# app/__init__.py

from flask_api import FlaskAPI
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config


# initialize sql-alchemy
db = SQLAlchemy()

# variable login_manager assigned an instance of class LoginManager
# login_manager = LoginManager()


def create_app(config_name):
    """Function to start the app

    :param config_name: dictionary key value picked up at run
    """

    # variable app assigned an instance of class flask
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    # login_manager.init_app(app)
    # login_manager.login_message = "You must be logged in to access this page."
    # login_manager.login_view = "auth.login"

    # from app import models
    # from .home import home as home_blueprint
    # app.register_blueprint(home_blueprint)

    """from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint) """

    return app
