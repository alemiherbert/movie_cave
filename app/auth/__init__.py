#!/usr/bin/python3

from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__)
from app.auth import routes