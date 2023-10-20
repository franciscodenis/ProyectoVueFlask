from flask import render_template, flash, redirect, url_for, abort
from src.core import services
from flask import Blueprint
from flask import request
from src.web.forms import ServiceForm
from src.web.helpers.auth import login_required, has_permission
from src.web.helpers.maintenance import maintenance_mode_guard

services_bp = Blueprint("servicios", __name__, url_prefix="/services")

@services_bp.get("/")
@login_required
@maintenance_mode_guard
def service_index():
    """
    Permita listar los servicios de forma paginada.
    """
    if not has_permission(["service_index"]):
        return abort(401)
    
    page = request.args.get('page', 1, type=int)

    pagination = services.list_services(page)

    servicios = pagination.items

    return render_template("services/index.html", servicios=servicios, pagination=pagination)

@services_bp.get("/<int:service_id>")
@login_required
@maintenance_mode_guard
def service_show(service_id):
    """
    Permite acceder a un servicio
    """
    if not has_permission(["service_show"]):
        return abort(401)

    servicio = services.get_service_by_id(service_id)
    if not servicio:
        flash('El servicio no se encontró.', 'danger')
        return redirect(url_for('servicios.service_index'))

    return render_template('services/show.html', servicio=servicio)

@services_bp.route('/update/<int:service_id>', methods=['GET', 'POST'])
@login_required
@maintenance_mode_guard
def service_update(service_id):
    """
    Permite actualizar un servicio por nombre
    """
    if not has_permission(["service_show"]):
        return abort(401)

    servicio_actual = services.get_service_by_id(service_id)
    form = ServiceForm(obj=servicio_actual)

    if form.validate_on_submit():
        if not has_permission(["service_update"]):
            flash('No tienes los permisos necesarios para editar el servicio', 'danger')
        else:
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
@login_required
@maintenance_mode_guard
def service_create():
    """
    Permite crear un servicio
    """
    if not has_permission(["service_create"]):
        return abort(401)

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
@login_required
@maintenance_mode_guard
def service_delete(service_id):
    """
    Permite eliminar un servicio por nombre
    """
    if not has_permission(["service_destroy"]):
        return abort(401)

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
