from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, HiddenField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class ServiceForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    description = StringField('Descripción', validators=[DataRequired()])
    keywords = StringField('Palabras clave (separadas por coma)', validators=[DataRequired()])
    service_type = SelectField('Tipo de Servicio', choices=[("ANALISIS", 'Análisis'), ("CONSULTORIA", 'Consultoría'), ("DESARROLLO", 'Desarrollo')], validators=[DataRequired()])
    enabled = BooleanField('Habilitado', default=True)
    submit = SubmitField('Crear Servicio')
    service_id = HiddenField('service_id')

class InstitutionForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    information = StringField('Informacion', validators=[DataRequired()])
    address = StringField('Dirección', validators=[DataRequired()])
    location = StringField('Dirección', validators=[DataRequired()])
    web = StringField('web', validators=[DataRequired()])
    keywords = StringField('Palabras Clave', validators=[DataRequired()])
    opening_hours = StringField('Dias y Horarios', validators=[DataRequired()])
    contact = StringField('Información de contacto', validators=[DataRequired()])
    has_authorization = BooleanField('Habilitado', default=True)
    submit = SubmitField('Crear Institucion')
    institution_id = HiddenField('institution_id')

class InstitutionSwitchForm(FlaskForm):
    institution = SelectField('Institución', validators=[DataRequired()])
    submit = SubmitField('Cambiar institución')

class UserForm(FlaskForm):
    first_name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellido', validators=[DataRequired()])
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    active = BooleanField('active', default=True)
    email = StringField('email')
    user_id = HiddenField('user_id')

class ConfigForm(FlaskForm):
    items_per_page = IntegerField(
        'Elementos por página',
        validators=[DataRequired(),
        NumberRange(min=2, max=20, message='El valor debe estar entre 2 y 20')]
    )
    contact_info = StringField('Información de Contacto')
    maintenance_mode = BooleanField('Modo de Mantenimiento', default=False)
    maintenance_message = StringField('Mensaje de Mantenimiento')
    submit = SubmitField('Guardar Configuración')