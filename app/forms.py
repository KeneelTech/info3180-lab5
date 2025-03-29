# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired



class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Upload Movie Poster', validators=[
            FileRequired(),
            FileAllowed(['jpg','pdf'], 'Only Images Of A Movie Poster To Be Uploaded')
    ])