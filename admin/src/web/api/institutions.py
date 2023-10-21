from flask import render_template, flash, redirect, url_for
from src.core import institutions
from flask import Blueprint
from src.web.schemas.institutions import institutions_schema
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
    list_inst = institutions.list_institutions()
    data = institutions_schema.dump(list_inst)
    print()
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    print(data)
    print("dataaaa--. eleeeen")

    from_institution = (len(data) // per_page) * (page - 1)
    to_institution = (len(data) // per_page) * (page)
    body_response = {}
    body_response["data"] = data[from_institution:to_institution]
    body_response["page"] = page
    body_response["per_page"] = per_page
    return body_response, 200


@api_instituciones_bp.route("/create", methods=["GET", "POST"])
def institution_create():
    """
    Permite accede al index(listado) del módulo de instituciones
    """
    new_data = request.get_json()
    print("new data: ------>", new_data)
    result = institutions.create_institution(**new_data)

    super_admins = list_super_admins()
    super_admin_role = find_role_by_name("Super Administrador")
    for super_admin in super_admins:
        set_user_roles(super_admin, result.id, [super_admin_role.id])

    print(result)
    return ({"status": "ok"}, 201)
