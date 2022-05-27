from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flashMarket.models import User

class RegisterForm(FlaskForm):
    def validate_name(self, name_to_check):
        print("Ima erer")
        print(name_to_check)
        user_name = User.query.filter_by(name=name_to_check.data).first()
        if user_name:
            raise ValidationError('User name already exists')

    def validate_email(self, email_to_check):
        email_id = User.query.filter_by(email_field=email_to_check.data).first()
        if email_id:
            raise ValidationError('Email already exists')

    name = StringField(label='username',validators=[Length(min=2, max=10), DataRequired()])
    email = StringField(label='EmailField', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    name  = StringField(label='username')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Login')

class PurchseForm(FlaskForm):
    submit = SubmitField(label='purchase')

class SellForm(FlaskForm):
    submit = SubmitField(label='sell')
