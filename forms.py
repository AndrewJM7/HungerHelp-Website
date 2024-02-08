from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_uploads import IMAGES, UploadSet, configure_uploads
from app import app

images = UploadSet('images', IMAGES)
configure_uploads(app, images)


class RecipeForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    recipe = StringField(validators=[DataRequired()])
    ingredients = StringField(validators=[DataRequired()])
    image = FileField(validators=[
        FileAllowed(images, "only images are allowed"),
        FileRequired("file field should not be empty")
    ])
    price = StringField(validators=[DataRequired()])
    submit = SubmitField()

