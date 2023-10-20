from flask import render_template, flash, redirect, url_for, abort
from src.core import service_requests
from flask import Blueprint
from flask import request
from src.web.forms import ServiceRequestForm
from src.web.helpers.auth import login_required, has_permission
from src.web.helpers.maintenance import maintenance_mode_guard

service_requests_bp = Blueprint(
    "service_requests", __name__, url_prefix="/service_requests"
)


@service_requests_bp.route("/")
@login_required
@maintenance_mode_guard
def service_requests_index():
    """
    Permita listar las solicitudes de servicio de forma paginada.
    Tambien permite filtrar por tipo de servicio, fecha de inicio, fecha de fin,
    estado y usuario.
    """
    if not has_permission(["service_requests_index"]):
        return abort(401)

    page = request.args.get("page", 1, type=int)
    service_type = request.args.get("service_type")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    state = request.args.get("state")
    user_id = request.args.get("user_id")

    pagination = service_requests.list_service_request(
        page, service_type, start_date, end_date, state, user_id
    )
    servicios = pagination.items

    return render_template(
        "service_requests/index.html", servicios=servicios, pagination=pagination
    )


@service_requests_bp.get("/<int:request_id>")
@login_required
@maintenance_mode_guard
def service_request_show(request_id):
    """
    Permite acceder a una solicitud de servicio
    """
    if not has_permission(["service_request_show"]):
        return abort(401)

    service_request = service_requests.get_service_request(request_id)
    if not service_request:
        flash("La solicitud de servicio no se encontró.", "danger")
        return redirect(url_for("service_requests.service_requests_index"))

    return render_template(
        "service_requests/show.html", service_request=service_request
    )


@service_requests_bp.route("/update/<int:request_id>", methods=["GET", "POST"])
@login_required
@maintenance_mode_guard
def service_request_update(request_id):
    """
    Permite actualizar la información de una solicitud de servicio
    """
    if not has_permission(["service_request_update"]):
        return abort(401)

    service_request = service_requests.get_service_request(request_id)
    form = ServiceRequestForm(obj=service_request)

    if form.validate_on_submit():
        # Procesa los datos del formulario y actualiza la solicitud de servicio en la base de datos
        new_data = {
            "title": form.title.data,
            "description": form.description.data,
            "status": form.status.data,
            "notes": form.notes.data,
        }

        result = service_requests.update_service_request(request_id, new_data)

        if result:
            flash(
                "La solicitud de servicio se ha actualizado correctamente.", "success"
            )
            return redirect(url_for("service_requests.service_requests_index"))
        else:
            flash("Hubo un error al actualizar la solicitud de servicio.", "danger")
    else:
        print(form.errors)

    return render_template(
        "service_requests/update.html", form=form, service_request=service_request
    )


@service_requests_bp.route("/destroy/<int:request_id>", methods=["GET"])
@login_required
@maintenance_mode_guard
def service_request_delete(request_id):
    """
    Permite eliminar una solicitud de servicio
    """
    if not has_permission(["service_request_destroy"]):
        return abort(401)

    request_a_eliminar = service_requests.delete_service_request(request_id)

    if request_a_eliminar:
        resultado = service_requests.delete_service_request(request_id)
        if resultado:
            flash("La solicitud de servicio se ha eliminado correctamente.", "success")
        else:
            flash("Hubo un error al eliminar la solicitud de servicio.", "danger")
    else:
        flash("La solicitud de servicio no se encontró.", "danger")

    return redirect(url_for("service_requests.service_request_index"))
