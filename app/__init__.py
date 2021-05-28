from flask import Flask
from config import Config
from app.database import db

app = Flask(__name__)
app.config.from_object(Config)

# Initiliaze the database
db.init_app(app)

# Must be at the end to avoid circular import
from app import routes
