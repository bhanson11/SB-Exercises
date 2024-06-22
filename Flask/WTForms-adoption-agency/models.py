from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    """pet for adoption"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.Text(), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    """Connect to database. this way we don't need a separate init.py"""
    
    db.app = app
    db.init_app(app)