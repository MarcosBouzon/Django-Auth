from wtforms import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, InputRequired, ValidationError, EqualTo



def _validate_first(value:str):
    if not value.replace(" ", "").isalpha():
        raise ValidationError("Only letters are allowed for this field")
def _validate_phone(value:str):
    if not value.isnumeric():
        raise ValidationError("Phone field can only contain numbers")


class LoginForm(Form):
    email = StringField(label="email", validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField()

class RegisterForm(Form):
    first = StringField("First Name", validators=[InputRequired()])
    last = StringField("Last Name", validators=[InputRequired()])
    email = EmailField("Email Address", validators=[Email("Invalid email")])
    phone = StringField("Phone Number", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    zip_code = StringField("Zip Code", validators=[InputRequired()])
    country = StringField("Country", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm = PasswordField("Confirm Password", validators=[EqualTo("password", "Passwords don't match")])
    submit = SubmitField()

    # custom validators
    def validate_first(self, field):
        return _validate_first(field.data)
    def validate_last(self, field):
        return _validate_first(field.data)
    def validate_country(self, field):
        return _validate_first(field.data)
    def validate_phone(self, field):
        return _validate_phone(field.data)



