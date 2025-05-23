from flask import abort
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from src.core import auth
from src.web.helpers.auth import login_required
from src.web.helpers.auth import has_permission
from src.web.helpers.auth import has_system_permission
from src.web.helpers.maintenance import maintenance_mode_guard
from src.web.forms import UserForm
from flask import request

user_bp = Blueprint("users", __name__, url_prefix="/usuarios")


@user_bp.get("/")
@login_required
@maintenance_mode_guard
def index():
    """
    Permite listar los usuarios de forma paginada.
    """
    if not has_system_permission(["user_index"]):
        return abort(401)

    page = request.args.get("page", 1, type=int)
    pagination = auth.list_users(page)
    users = pagination.items

    return render_template("users/index.html", users=users, pagination=pagination)

@user_bp.get("/<int:user_id>")
@login_required
@maintenance_mode_guard
def show(user_id):
    """
    Permite acceder a un usuario
    """
    if not has_system_permission(["user_show"]):
        return abort(401)

    user = auth.get_user_by_id(user_id)
    if not user:
        flash("El usuario no se encontró.", "danger")
        return redirect(url_for("users.index"))

    return render_template("users/show.html", user=user)

@user_bp.route("/update/<int:user_id>", methods=["GET", "POST"])
@login_required
@maintenance_mode_guard
def update(user_id):
    """
    Permite actualizar un usuario
    """
    if not has_system_permission(["user_show"]):
        return abort(401)

    usuario_actual = auth.get_user_by_id(user_id)
    form = UserForm(obj=usuario_actual)

    if form.validate_on_submit():
        if not has_system_permission(["user_update"]):
            flash("No tienes los permisos necesarios para editar el usuario", "danger")
        else:
            new_data = {
                "first_name": form.first_name.data,
                "last_name": form.last_name.data,
                "username": form.username.data,
                "active": form.active.data,
            }

            print(new_data)

            result = auth.update_user(user_id, new_data)

            if result:
                flash("El usuario se ha actualizado correctamente.", "success")
                return redirect(url_for("users.index"))
            else:
                flash("Hubo un error al actualizar el usuario", "danger")
    else:
        print(form.errors)

    return render_template("users/update.html", form=form, user=usuario_actual)


@user_bp.get("/destroy/<int:user_id>")
@login_required
@maintenance_mode_guard
def delete(user_id):
    """
    Permite eliminar un usuario por id
    """
    if not has_system_permission(["user_destroy"]):
        return abort(401)

    user_a_eliminar = auth.get_user_by_id(user_id)
    if user_a_eliminar:
        if user_a_eliminar.system_roles:
            flash("No se pueden eliminar usuarios de sistema", "danger")
        else:
            resultado = auth.delete_user(user_id)
            if resultado:
                flash("El usuario se ha eliminado correctamente", "success")
            else:
                flash("Hubo un error al eliminar el usuario", "danger")
    return redirect(url_for("users.index"))
