#!/usr/bin/python3

"""This module contains the User model class"""

from typing import Optional
from app import db, login
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users' 
    # SQLAlchemy requires this sort of static typing thing
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(128), unique=True, index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(128), unique=True, index=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # Relationships
    # With time, we should be able to know which movies a user has watched
    # and the genres of movies the user watches so we can recommend movies
    # to the user based on these.
    # movies = so.relationship('Movie', backref='user', lazy='dynamic')

def __str__(self):
    return "<User {}>".format(self.username)

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)


class SuperUser(User):
    """The admin class"""
    pass


@login.user_loader
def load_user(id):
    return db.session.query(User).get(int(id))