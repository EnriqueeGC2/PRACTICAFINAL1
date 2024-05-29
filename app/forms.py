from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    direccion = StringField('Dirección')
    telefono = StringField('Teléfono')
    correoelectronico = StringField('Correo Electrónico')
    submit = SubmitField('Guardar')
