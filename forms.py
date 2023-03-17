"""Forms for adopt app."""
#unused imports
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Name",
        validators=[InputRequired()]
    ) # Add spacing to improve style
    species = SelectField(
        "Species",
        choices=[('dog', 'Dog'),
                 ('cat', 'Cat'),
                 ('porcupine', 'Porcupine')],
        validators=[InputRequired(), AnyOf([
            'dog',
            'cat',
            'porcupine'
        ], "We only accept dogs, cats, and porcupines! Sorry.")] # By default selectfield w/ enforce choices
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
    notes = StringField("Notes") # Add optional validator


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField(
        "Photo link",
        validators=[Optional(), URL()]
    )

    notes = StringField("Notes") # Add optional validator

    available = BooleanField('Available')


    # QUESTION: How to add select field that would handle booleans?
    # available = SelectField(
    #     "Availability",
    #     choices=[(True, 'Available'),
    #              (False, 'Not Available')]
    # )