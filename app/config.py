#!/usr/bin/env python3
"""Application configuration."""

from app import db
from os import environ, path

class BaseConfig:
    """Base configuration.
    
    Use a SQLite database for early development.
    """
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or \
        'sqlite:///' + path.join(path.dirname(__file__), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(path.dirname(__file__), 'dev.db')

class TestConfig(BaseConfig):
    """Test configuration."""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(path.dirname(__file__), 'test.db')
