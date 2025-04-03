from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    year = db.Column(db.Integer)
    length = db.Column(db.Integer)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<Movie {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'length': self.length,
            'description': self.description
        }
