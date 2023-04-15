from flask import Flask
from .routers import main
from .extentions import db


def create_app():
    app = Flask(__name__)

    app.config.from_object('myapp.settings')
    
    db.init_app(app)

    app.register_blueprint(main)

    return app