from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for
from src.web.helpers.auth import has_permission, login_required
from src.core import auth
from src.web.forms import MemberForm

members_bp = Blueprint("members", __name__, url_prefix="/members")

@members_bp.get("/")
@login_required
def member_index():
    if not has_permission(["member_index"]):
        return abort(401)

    page = request.args.get('page', 1, type=int)
    institution_id = session["institution"]

    # pagination = list_institution_members(page, institution_id)
    pagination = auth.list_institution_users(institution_id, page)

    members = pagination.items

    print(members)

    return render_template("members/index.html", members=members, pagination=pagination)

@members_bp.get("/")
@login_required
def member_create():
    if not has_permission(["member_create"]):
        return abort(401)

    # TODO: Hacer
    return redirect("home")


@members_bp.route("/update/<int:user_id>", methods=["GET", "POST"])
@login_required
def member_update(user_id):
    """
    Permite cambiar el rol de un usuario en la institución
    """
    if not has_permission(["member_show"]):
        return abort(401)

    usuario_actual = auth.get_user_by_id(user_id)
    institution_id = session["institution"]
    rol_actual = auth.list_institution_user_roles(user_id, institution_id).first()
    roles_disponibles = auth.list_roles()
    roles = []
    for rol in roles_disponibles:
        if rol.name != "Super Administrador":
            roles.append((
                rol.id,
                rol.name
            ))
    form = MemberForm(obj=usuario_actual)
    form.role.choices = roles

    if form.validate_on_submit():
        if not has_permission(["member_update"]):
            flash("No tienes los permisos necesarios para editar el miembro", "danger")
        else:
            # rol_seleccionado = dict(form.role.choices).get(int(form.role.data))
            # print(dict(form.role.choices))
            # print("revisar")
            # print(rol_seleccionado)
            # print("revisar")
            # rol = {
            #     "id": rol_seleccionado[0],
            #     "name": rol_seleccionado[1]
            # }

            # Llamar a update de miembro
            auth.replace_user_roles(usuario_actual, institution_id, [form.role.data])
            flash("El miembro ha sido modificado correctamente", "success")
            return redirect(url_for("members.member_index"))

    if rol_actual:
        form.role.data = str(rol_actual.id)

    return render_template("members/edit.html", form=form)


@members_bp.get("/remove/<int:user_id>")
@login_required
def member_remove(user_id):
    """
    Permite remover un miembro de la institución
    """

    if not has_permission(["member_destroy"]):
        return abort(401)

    institution_id = session["institution"]
    auth.remove_member(user_id, institution_id)

    flash("El miembro fue removido de la institución correctamente", "success")
    return redirect(url_for("members.member_index"))
