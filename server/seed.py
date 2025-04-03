#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Movie

fake = Faker()

def make_movies():

    print("Deleting existing movies...")
    Movie.query.delete()

    print("Creating movies...")
    movies = [
        Movie(
            title="The Shawshank Redemption",
            year=1994,
            length=142,
            description="Two imprisoned men bond over a number of years..."
        ),
        Movie(
            title="The Godfather",
            year=1972,
            length=175,
            description="The aging patriarch of an organized crime dynasty..."
        )
    ]

    db.session.add_all(movies)
    db.session.commit()
    print("Movies seeded successfully!")

if __name__ == '__main__':
    with app.app_context():
        make_movies()
