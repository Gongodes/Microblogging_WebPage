from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    title = StringField('Titulo',validators=[DataRequired()])
    text= TextAreaField('Contenido',validators=[DataRequired()])
    submit = SubmitField('Postear')