from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UserText(FlaskForm):
    text = StringField("Enter text", validators=[DataRequired(), Length(min=1, max=256)])
    submit = SubmitField("Encrypt")