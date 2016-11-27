from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("Must enter a first name")])
    last_name = StringField('Last name', validators=[DataRequired("Must enter a last name")])
    email = StringField('Email', validators=[DataRequired("Must enter a valid email address"), Email("Incorrect format for email")])
    password = PasswordField('Password', validators=[DataRequired("Password is incorrect"), 
    												 Length(min=6, message="Password must be 6 characters or more")])
    submit = SubmitField('Sign up')
