from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired])
    species = StringField("Species", validators=[InputRequired])
    photo_url = StringField("Photo URL")
    age = IntegerField('Age')
    notes = TextAreaField('Notes')