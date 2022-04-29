from flask import Flask
from .routes.views import views_bp

port = 8000

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True

    #Register of the Blueprints

    app.register_blueprint(views_bp)


    return app


app = create_app()