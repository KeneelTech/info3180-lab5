# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime


class MovieDatabase(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(600))
    poster = db.Column(db.String(120))
    created_at = db.Column(db.DateTime)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


def __repr__(self):
        return f"<Movie {self.title}>"