from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField
from datetime import datetime

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    login_submit = SubmitField('Login')

class BmForm(FlaskForm):
    meet_date = DateField('{}'.format(datetime.now().strftime('%Y-%m-%d')))
    thought = StringField('Spritual Thought Assignment')
    agenda = TextAreaField('Agenda Items')
    