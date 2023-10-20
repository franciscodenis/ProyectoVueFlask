from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for
from src.web.helpers.auth import has_permission, login_required
from src.core import auth
from src.web.forms import MemberForm, MemberAddForm
from src.web.helpers.maintenance import maintenance_mode_guard

members_bp = Blueprint("members", __name__, url_prefix="/members")

@members_bp.get("/")
@login_required
@maintenance_mode_guard
def member_index():
    if not has_permission(["member_index"]):
        return abort(401)

    page = request.args.get('page', 1, type=int)
    institution_id = session["institution"]

    pagination = auth.list_institution_users(institution_id, page)

    members = pagination.items

    print(members)

    return render_template("members/index.html", members=members, pagination=pagination)

@members_bp.route("/add", methods=["GET", "POST"])
@login_required
@maintenance_mode_guard
def member_create():
    if not has_permission(["member_create"]):
        return abort(401)

    institution_id = session["institution"]
    users = []
    users_not_in_institution = auth.list_users_not_in_institution(institution_id).all()
    if len(users_not_in_institution) == 0:
        flash("No hay usuarios disponibles para agregar como miembros a la institución", "warning")
    for user in users_not_in_institution:
        users.append((
            user.id,
            user.email
        ))

    roles = []
    roles_disponibles = auth.list_roles()
    for role in roles_disponibles:
        if role.name != "Super Administrador":
            roles.append((
                role.id,
                role.name
            ))

    form = MemberAddForm()
    form.email.choices = users
    form.role.choices = roles

    if form.validate_on_submit():
        user = auth.get_user_by_id(form.email.data)
        auth.set_user_roles(user, institution_id, [form.role.data])
        flash("Se agregó el miembro a la institución correctamente", "success")
        return redirect(url_for("members.member_index"))

    return render_template("members/add.html", form=form)


@members_bp.route("/update/<int:user_id>", methods=["GET", "POST"])
@login_required
@maintenance_mode_guard
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
            # Llamar a update de miembro
            auth.replace_user_roles(usuario_actual, institution_id, [form.role.data])
            flash("El miembro ha sido modificado correctamente", "success")
            return redirect(url_for("members.member_index"))

    if rol_actual:
        form.role.data = str(rol_actual.id)

    return render_template("members/edit.html", form=form)


@members_bp.get("/remove/<int:user_id>")
@login_required
@maintenance_mode_guard
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
