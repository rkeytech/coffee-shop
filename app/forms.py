from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, PasswordField
from wtforms.validators import DataRequired, Email


class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    job = StringField('Job', validators=[DataRequired()])
    wage = DecimalField('Wage', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
