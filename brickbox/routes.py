# Set up following Code Institute walkthrough project tutorials

from flask import render_template
from brickbox import app, db


@app.route("/")
def home():
    return render_template("base.html")