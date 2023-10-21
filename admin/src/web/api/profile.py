from flask import render_template, flash, redirect, url_for
from src.core import auth
from flask import Blueprint
from src.web.schemas.profile import user_schema
from flask import request


api_usuarios_bp = Blueprint("users_api", __name__, url_prefix="/api/consultas_usuarios")


@api_usuarios_bp.get("/")
def user_by_id():
    """
    Accede al perfil del usuario dado un token
    """
    user_by_id = auth.get_user_by_id(1)
    data = user_schema.dump(user_by_id)
    return data, 200
