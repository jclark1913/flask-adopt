"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

def Pet(Model.db):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(24),
        nullable=False
    )

    species = db.Column(
        db.String(24),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=""
    )

    # Limit pool of choices
    age = db.Column(
        db.Text,
        nullable=False
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )