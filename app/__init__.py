from flask import Flask
from config import Config
from app.database import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Initiliaze the database
db.init_app(app)
migrate = Migrate(app, db)

# Must be at the end to avoid circular import
from app import routes
