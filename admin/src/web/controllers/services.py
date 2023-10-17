from flask import render_template, flash, redirect, url_for
from src.core import services
from flask import Blueprint
from flask import request
from src.web.forms import ServiceForm

services_bp = Blueprint("servicios", __name__, url_prefix="/services")

@services_bp.get("/")
def service_index():
    """
    Permite accede al index(listado) del módulo de servicios
    """
    servicios = services.list_services()
    return render_template("services/index.html",servicios=servicios)

@services_bp.route('/update/<int:service_id>', methods=['GET', 'POST'])
def service_update(service_id):
    """
    Permite actualizar un servicio por nombre
    """
    servicio_actual = services.get_service_by_id(service_id)
    #print(service_id)
    form = ServiceForm(obj=servicio_actual)
    
    if form.validate_on_submit():
        
        # Procesa los datos del formulario y actualiza el servicio en la base de datos
        new_data = {
            'name': form.name.data,
            'description': form.description.data,
            'keywords': form.keywords.data,
            'service_type': form.service_type.data,
            'enabled': form.enabled.data
        }
        print(new_data)

        result = services.update_service(service_id, new_data)
        
        if result:
            flash('El servicio se ha actualizado correctamente.', 'success')
            return redirect(url_for('servicios.service_index'))
        else:
            flash('Hubo un error al actualizar el servicio.', 'danger')
    else :
        print(form.errors)
    
    return render_template('services/update_service.html', form=form, servicio=servicio_actual)

@services_bp.route('/create', methods=['GET', 'POST'])
def service_create():
    """
    Permite crear un servicio
    """
    form = ServiceForm()
    if form.validate_on_submit():
        # Procesa los datos del formulario y crea el servicio en la base de datos
        new_data = {
            'name': form.name.data,
            'description': form.description.data,
            'keywords': form.keywords.data,
            'service_type': form.service_type.data,
            'enabled': form.enabled.data
        }

        result = services.create_service(**new_data)
        
        if result:
            flash('El servicio se ha creado correctamente.', 'success')
            return redirect(url_for('servicios.service_index'))
        else:
            flash('Hubo un error al crear el servicio.', 'danger')
    
    return render_template('services/create_service.html', form=form)

@services_bp.route('/destroy/<int:service_id>', methods=['GET'])
def service_delete(service_id):
    """
    Permite eliminar un servicio por nombre
    """
    servicio_a_eliminar = services.get_service_by_id(service_id)
    if servicio_a_eliminar:
        resultado = services.delete_service(service_id)
        if resultado:
            flash('El servicio se ha eliminado correctamente.', 'success')
        else:
            flash('Hubo un error al eliminar el servicio.', 'danger')
    else:
        flash('El servicio no se encontró.', 'danger')
    
    return redirect(url_for('servicios.service_index'))
