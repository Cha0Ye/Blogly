"""Seed file to make sample data for pets db."""

from models import User, db
from app import app

# Create all tables
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
alan = User(first_name='Alan', last_name='Alda')
joel = User(first_name='Joel', last_name='Burton')
jane = User(first_name='Jane', last_name='Smith')

# Add new objects to session, so they'll persist
db.session.add(alan)
db.session.add(joel)
db.session.add(jane)

# Commit--otherwise, this never gets saved!
db.session.commit()