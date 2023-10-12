from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class ServiceForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    description = StringField('Descripción', validators=[DataRequired()])
    keywords = StringField('Palabras clave (separadas por coma)', validators=[DataRequired()])
    service_type = SelectField('Tipo de Servicio', choices=[("ANALISIS", 'Análisis'), ("CONSULTORIA", 'Consultoría'), ("DESARROLLO", 'Desarrollo')], validators=[DataRequired()])
    enabled = BooleanField('Habilitado', default=True)
    submit = SubmitField('Crear Servicio')
    service_id = HiddenField('service_id')