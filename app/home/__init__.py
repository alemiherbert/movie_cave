#!/usr/bin/python3

from flask import Blueprint
home_bp = Blueprint('home_bp', __name__)
from app.home import routes