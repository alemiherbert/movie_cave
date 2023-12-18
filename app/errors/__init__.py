#!/usr/bin/python3

from flask import Blueprint

error_bp = Blueprint('error_bp', __name__)
from app.errors import handlers