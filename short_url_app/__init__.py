from flask import Flask
from .extentions import db
from .config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(Config)
    
    db.init_app(app)

    from short_url_app.routers import main
    app.register_blueprint(main)

    return app