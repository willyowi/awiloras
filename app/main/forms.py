from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,IntegerField,SelectField
from wtforms.fields.html5 import DateField

#for the picture upload
from flask_wtf.file import FileField,FileAllowed

from wtforms import ValidationError
from wtforms.validators import DataRequired,Email
from ..models import User



class UpdateProfileForm(FlaskForm):
    '''
    class to create a form to update user details
    '''
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    picture=FileField('Update Profile Pic',validators=[FileAllowed(['jpg','png','jpeg','png'])])
    submit=SubmitField('Update')



class Session_typesForm(FlaskForm):
    '''
    class to know the type of session

    '''
    session=SelectField('Break or Work',choices=[('',''),('break','Break'),('work','Work')])
    submit=SubmitField('Type')



class SessionForm(FlaskForm):
    '''
    class to know which sessions and time

    '''
    task=TextAreaField('Whats your current task',validators=[DataRequired()])
    time=TextAreaField('how for hoe long?',validators=[DataRequired()])
    submit=SubmitField('Session')