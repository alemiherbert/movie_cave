#!/usr/bin/python3

from . import home_bp
from flask import render_template

@home_bp.route('/')
def index():
    return render_template("home/index.html")

@home_bp.route('/movies')
def movie():
    return render_template("home/movie.html")

@home_bp.route('/movie-details')
def movie_details():
    return render_template("home/movie_details.html")

@home_bp.route('/tv-shows')
def tv_shows():
    return render_template("home/tv_shows.html")