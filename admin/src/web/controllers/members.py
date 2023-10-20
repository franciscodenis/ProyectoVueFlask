from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for
from src.web.helpers.auth import has_permission
from src.core.auth import list_institution_users

members_bp = Blueprint("members", __name__, url_prefix="/members")

@members_bp.get("/")
def member_index():
    if not has_permission(["member_index"]):
        return abort(401)

    page = request.args.get('page', 1, type=int)
    institution_id = session["institution"]

    # pagination = list_institution_members(page, institution_id)
    pagination = list_institution_users(institution_id, page)

    members = pagination.items

    print(members)

    return render_template("members/index.html", members=members, pagination=pagination)

@members_bp.get("/")
def member_create():
    if not has_permission(["member_create"]):
        return abort(401)

    # TODO: Hacer
    return redirect("home")