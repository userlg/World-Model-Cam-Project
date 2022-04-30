from flask import Flask
from .routes.views import views_bp
from .routes.auth import auth_bp
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

from .config import DevelopmentConfig, ProductionConfig

from os import environ

import uuid

port = environ.get('PORT')
host = environ.get('HOST')

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    #app.config.from_object(ProductionConfig())
    db = MongoEngine(app)

    #Register of the Blueprints

    app.register_blueprint(views_bp)
    app.register_blueprint(auth_bp)


    return app


app = create_app()