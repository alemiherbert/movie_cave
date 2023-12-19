#!/usr/bin/env python3

"""Initialize app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate(db)
login = LoginManager()
login.login_view = 'auth_bp.login'

# Avoid a circular import
from .config import BaseConfig


def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(BaseConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    with app.app_context():
        from .errors import error_bp
        from .auth import auth_bp
        from .home import home_bp

        app.register_blueprint(error_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(home_bp)
    return app
