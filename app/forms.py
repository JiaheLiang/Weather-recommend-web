from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, RadioField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError,number_range
from app.models import Task

class DeleteEventForm(FlaskForm):
	eventid = StringField('enter username for delete')
	submit = SubmitField('Delete')