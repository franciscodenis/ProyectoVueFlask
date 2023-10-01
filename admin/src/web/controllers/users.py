from flask import Blueprint
from flask import render_template
from src.core.auth import list_users

user_bp = Blueprint("users", __name__, url_prefix="/usuarios")


@user_bp.get("/")
def index():
    users = list_users()
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
