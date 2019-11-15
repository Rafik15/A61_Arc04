from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ModelePredictionForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])

    submit = SubmitField('Predire')