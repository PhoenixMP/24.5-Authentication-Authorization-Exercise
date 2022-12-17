from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[
                           InputRequired('Please enter a username')])
    password = PasswordField("Password", validators=[
                             InputRequired('Please enter a password')])
    email = StringField("Email", validators=[
                        InputRequired('Please enter an email address')])
    first_name = StringField("First Name", validators=[
                             InputRequired('Please enter your first name')])
    last_name = StringField("Last Name", validators=[
                            InputRequired('Please enter your last name')])


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
                           InputRequired('Please enter a username')])
    password = PasswordField("Password", validators=[
                             InputRequired('Please enter a password')])


class FeedbackForm(FlaskForm):
    title = StringField("Feedback Title", validators=[
        InputRequired('Please enter title'), Length(max=100)])
    content = StringField("Feedback Text", validators=[
        InputRequired('Please enter feedback')])
