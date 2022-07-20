from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from string import ascii_letters, punctuation, digits
from .models import User
import re

class PostcodeFormat:
    def __call__(self, form, field):
        if field.data is None or field.data == "":
            return

        pattern = r"^[0-9][0-9]-[0-9][0-9][0-9]$"

        if re.search(pattern, field.data) is None:
            raise ValidationError("Wrong postcode!")


class UniqueLogin:
    def __call__(self, form, field):
        if field.data is None or field.data == "":
            return

        user = User.query.filter_by(login=field.data).first()
        if user:
            raise ValidationError("Account with this login exists!")


class PasswordFormat:
    def __call__(self, form, field):
        if field.data is None or field.data == "":
            return
        #jeden znak specjalny
        #jedna dowolna litera
        #jedna cyfra
        special = False
        letter = False
        digit = False
        for ch in field.data:
            if ch in ascii_letters:
                letter = True
            elif ch in punctuation:
                special = True
            elif ch in digits:
                digit = True

        if not letter or not special or not digit:
            raise ValidationError("Password has to have as least one digit, one special character and one letter")



class RegisterForm(FlaskForm):
    login = StringField('Login', [validators.DataRequired(), validators.Length(min=3, max=50), UniqueLogin()])
    password1 = PasswordField('Password', [validators.DataRequired(), validators.Length(min=7, max=50), validators.EqualTo('password2',message='Passwords must match'), PasswordFormat()])
    password2 = PasswordField('Password confirm', [validators.DataRequired(), validators.Length(min=7, max=50)])
    postcode = StringField('Postcode', [validators.DataRequired(), PostcodeFormat()])
class LoginForm(FlaskForm):
    login = StringField('Login', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', [validators.DataRequired()])
    new_password = PasswordField('New password', [validators.DataRequired(), validators.Length(min=7, max=50)])
    new_password_confirmation = PasswordField('New password confirmation', [validators.DataRequired(), validators.Length(min=7, max=50), validators.EqualTo('new_password',message='Passwords must match')])


#dodaj do formularza rejestracji pole z kodem pocztowym a nastepnie napisz do nigo wlasny walidator
#na konic spraw aby ten kod pocztowy zapisywal sie w bazie danych w tabeli User