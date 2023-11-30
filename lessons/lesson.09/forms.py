from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length


class CreateProductForm(FlaskForm):
    name = StringField('name', validators=[Length(max=3)])