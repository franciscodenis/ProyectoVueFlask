from flask import Blueprint, render_template, redirect, url_for, flash
from src.core import configuration
from src.web.forms import ConfigForm

configuration_bp = Blueprint('config', __name__, url_prefix="/config")

@configuration_bp.route("/", methods=['GET', 'POST'])
def config_update():
    # Obtén la configuración actual desde la base de datos o donde la tengas almacenada
    current_config = configuration.get_or_create_config()  # Implementa esta función

    form = ConfigForm(obj=current_config)

    if form.validate_on_submit():
        # Procesa los datos del formulario y actualiza la configuración
        new_config = {
            'items_per_page': form.items_per_page.data,
            'contact_info': form.contact_info.data,
            'maintenance_mode': form.maintenance_mode.data,
            'maintenance_message': form.maintenance_message.data
        }

        # Llama a una función para actualizar la configuración, implementa esta función
        result = configuration.update_config(new_config)  

        if result:
            flash('La configuración se ha actualizado correctamente.', 'success')
            return render_template('home.html')
        else:
            flash('Hubo un error al actualizar la configuración.', 'danger')

    return render_template('config.html', form=form)