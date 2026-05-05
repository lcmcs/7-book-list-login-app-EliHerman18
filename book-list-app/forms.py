from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message="Title is required."),
        Length(max=120, message="Title cannot exceed 120 characters.")
    ])
    author = StringField('Author', validators=[
        DataRequired(message="Author is required."),
        Length(max=80, message="Author cannot exceed 80 characters.")
    ])
    year = IntegerField('Year', validators=[
        DataRequired(message="Year is required."),
        NumberRange(min=1000, max=2100, message="Year must be between 1000 and 2100.")
    ])
    submit = SubmitField('Add Book')
