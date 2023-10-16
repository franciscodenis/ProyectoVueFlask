from flask import abort
from flask import Blueprint
from flask import render_template
from src.core import auth
from src.web.helpers.auth import login_required
from src.web.helpers.auth import has_permission

user_bp = Blueprint("users", __name__, url_prefix="/usuarios")


@user_bp.get("/")
@login_required
def index():
    if not has_permission(["user_index"]):
        return abort(401)

    users = auth.list_users()
    return render_template("users/index.html", users=users)


def show():
    pass


def new():
    pass


def create():
    pass


def edit():
    pass


def update():
    pass


def delete():
    pass
