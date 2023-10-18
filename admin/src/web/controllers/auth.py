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

@auth_bp.get("/validate")
def validate():

    email = request.args.get("email", None)
    key = request.args.get("key", None)

    if email and key:
        if auth.validate_email(email, key):
            flash("Email validado correctamente, ya puedes iniciar sesión", "success")
            return redirect(url_for("auth.login"))

    flash("Hubo un error al validar el usuario", "danger")
    return redirect(url_for("auth.login"))

@auth_bp.get("/register")
def register():
    return render_template("auth/register.html")

@auth_bp.post("/register")
def create():
    params = request.form

    print(params)

    user = auth.create_user_stub(params["email"], params["first_name"], params["last_name"])

    if not user:
        flash("No se pudo crear el usuario, verifique los datos", "danger")
        return redirect(url_for("auth.register"))

    flash("Usuario creado correctamente, se le ha enviado un email para su activación.", "info")
    return redirect(url_for("auth.login"))
