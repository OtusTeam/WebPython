from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField(
        "Product name",
        validators=[
            DataRequired(),
            Length(min=3, max=100),
        ],
    )
