"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Name",
        validators=[InputRequired()]
    )
    species = SelectField(
        "Species",
        choices=[('dog', 'Dog'),
                 ('cat', 'Cat'),
                 ('porcupine', 'Porcupine')],
        validators=[InputRequired(), AnyOf([
            'dog',
            'cat',
            'porcupine'
        ], "We only accept dogs, cats, and porcupines! Sorry.")]
    )
    photo_url = StringField(
        "Photo link",
        validators=[Optional(), URL()]
    )
    age = SelectField(
                'Age',
                choices=[('baby', 'Baby'),
                         ('young', 'Young'),
                         ('adult', 'Adult'),
                         ('senior', 'Senior')],
                validators=[AnyOf([
                    'baby',
                    'young',
                    'adult',
                    'senior'
                ], "We only accept pets who are young, babies, adults, or seniors! Sorry.")]
                )
    notes = StringField("Notes")