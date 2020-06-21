from flask import Flask
import os
from app.extensions import db
from app.api import api


def create_app(script_info=None):
    """Creates the FLask application Instance"""
    app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    extensions(app)

    return app


def extensions(app):
    """An extension for typing the external instances to application instance"""
    api.init_app(app)
    db.init_app(app)
