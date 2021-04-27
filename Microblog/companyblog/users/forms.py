from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed



from flask_login import current_user
from companyblog.models import User

class LoginForm(FlaskForm):
    email= StringField('Email',validators=[DataRequired(),Email()])
    password= PasswordField('Contraseña',validators=[DataRequired()])
    submit= SubmitField('Ingresar')

class RegistrationForm(FlaskForm):
    email= StringField('Correo',validators=[DataRequired(),Email()])
    username= StringField('Usuario',validators=[DataRequired()])
    password= PasswordField('Contraseña',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match')])
    pass_confirm=PasswordField('Confirmar Contraseña',validators=[DataRequired()])
    submit = SubmitField('Registrar !')


    def check_email(self,field):
        if User.query.filter_by(email=field).first():
            raise ValidationError('Tu Correo, ya ha sido registrado!')

        def check_username(self,field):
            if User.query.filter_by(username=field).first():
                raise ValidationError('Tu usaurio ya ha sido registrado!')  

class UpdateUserForm(FlaskForm):
    email= StringField('Correo',validators=[DataRequired(),Email()])
    username= StringField('Usuario',validators=[DataRequired()])
    picture=FileField('Actualizar foto de perfil', validators=[FileAllowed(['jpg', 'png'])])
    submit= SubmitField('Actualizar')

    def check_email(self,field):
        if User.query.filter_by(email=field).first():
            raise ValidationError('Tu Correo, ya ha sido registrado!')

    def check_username(self,field):
        if User.query.filter_by(username=field).first():
            raise ValidationError('Tu usaurio ya ha sido registrado!') 


