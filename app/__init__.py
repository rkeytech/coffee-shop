from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path

# Initialize database
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register the blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Initiliaze the database
    db.init_app(app)
    migrate = Migrate(app, db)

    from .models import User
    create_database(app)

    return app


def create_database(app):
    if not path.exists(f'{path.dirname(__file__)}.db'):
        db.create_all(app=app)
        print("Database created successfully!")
