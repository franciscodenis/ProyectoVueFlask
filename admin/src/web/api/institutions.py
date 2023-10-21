from flask import render_template, flash, redirect, url_for
from src.core import institutions
from flask import Blueprint
from src.web.schemas.institutions import institutions_schema
from src.web.schemas.institutions import create_institutions_schema,create_institution_schema
from src.core.auth import list_super_admins, find_role_by_name, set_user_roles
from flask import request


api_instituciones_bp = Blueprint(
    "institutions_api", __name__, url_prefix="/api/consultas_instituciones"
)


@api_instituciones_bp.get("/")
def institution_index():
    """
    Permite accede al index(listado) del módulo de instituciones
    """

    page = 1
    per_page = 10
    if request.args.get('page'):
        page = int(request.args.get('page'))
    if request.args.get('per_page'):
        per_page = int(request.args.get('per_page'))

    list_inst = institutions.list_institutions(page,per_page)
    data = institutions_schema.dump(list_inst)
    body_response = {}
    body_response["data"] = data
    body_response["page"] = page
    body_response["per_page"] = per_page
    body_response["total"] = institutions.institution_count()
    return body_response,200


@api_instituciones_bp.route("/create", methods=["GET", "POST"])
def institution_create():
    """
    Toma la información del request, valida con el schema "create_institution_schema", y guarda en la base de datos.
    """
    new_data = request.get_json()
    new_institution = create_institution_schema.load(new_data)
    result = institutions.create_institution(**new_data)

    super_admins = list_super_admins()
    super_admin_role = find_role_by_name("Super Administrador")
    for super_admin in super_admins:
        set_user_roles(super_admin, result.id, [super_admin_role.id])

    return ({"status": "ok"}, 201)
