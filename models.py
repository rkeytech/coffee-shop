from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    job = db.Column(db.String(50), nullable=False)
    wage = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Name: {self.last_name}>'
