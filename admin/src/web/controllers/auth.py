from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import session
from src.core import auth

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.get("/")
def login():
    return render_template("auth/login.html")

@auth_bp.post("/authenticate")
def authenticate():
    params = request.form

    user = auth.check_user(params["email"], params["password"])

    if not user:
        flash("Email o clave incorrecta.", "danger")
        return redirect(url_for("auth.login"))

    session["user"] = user.email
    flash("La sesión se inició correctamente", "success")
    return redirect(url_for("home"))

@auth_bp.get("/logout")
def logout():
    if session.get("user"):
        del session["user"]
        session.clear()
        flash("La sesión se cerró correctamente.", "info")
    else:
        flash("No hay sesión iniciada", "info")

    return redirect(url_for("auth.login"))
