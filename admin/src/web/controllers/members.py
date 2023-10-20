from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for
from src.web.helpers.auth import has_permission, login_required
from src.core import auth

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