"""Flask app for adopt app."""

import os

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def homepage():
    """Render the homepage with listing of available pets."""

    return render_template(
        "homepage.html",
        pets=Pet.query.all()
    )

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Pet add form, handles adding pets"""

    return render_template(
        "add_pet.html"
    )

