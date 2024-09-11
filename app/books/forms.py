from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(2, 40)])
    cover_photo= FileField("Cover Photo")
    pages_number= IntegerField("Number Of Pages", validators=[DataRequired()])
    description = StringField("Description")
    submit = SubmitField("Submit")
   