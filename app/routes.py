from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/FAV")
def fav5():
    games = ['Dark Souls 3', 'Destiny 2', 'Elden Ring', 'Cup Head', 'Ninja Gaiden']

    return render_template('FAV.html', names=games)