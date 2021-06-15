from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(50), nullable=False, default="No number")
    address = db.Column(db.String(50), nullable=False, default="No Address")
    password = db.Column(db.String(150), nullable=False)
    job = db.Column(db.String(50), nullable=False)
    wage = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Name: {self.last_name}>'
