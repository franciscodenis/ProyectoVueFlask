from flask import render_template, flash, redirect, url_for
from src.core import services

from src.core.configuration import get_items_per_page
from flask import Blueprint
from src.web.schemas.services import service_schemas, service_schema
from src.core.services.service import ServiceType
from flask import request

api_services_bp = Blueprint("services_api", __name__, url_prefix="/api/services")


@api_services_bp.get("/search")
def service_search():
    """
    Permite accede al index(listado) del módulo de instituciones
    """

    page = 1
    per_page = get_items_per_page()
    if request.args.get("page"):
        page = int(request.args.get("page"))
    if request.args.get("per_page"):
        per_page = int(request.args.get("per_page"))
    q = ""
    if request.args.get("q"):
        q = str(request.args.get("q"))
    type = ""
    if request.args.get("type"):
        type = str(request.args.get("type"))

    list_services = services.list_service_search(
        search=q, type=type, page=page, per_page=per_page
    )
    data = service_schemas.dump(list_services)
    body_response = {}
    body_response["data"] = data
    body_response["page"] = page
    body_response["per_page"] = per_page
    body_response["total"] = services.services_count()
    return body_response, 200


@api_services_bp.get("/<int:id>")
def service_by_id(id):
    if not id:
        return "id is required", 400

    service_by_id = services.get_service_by_id(id)
    data = service_schema.dump(service_by_id)
    return data, 200


@api_services_bp.get("/services-types")
def service_type():
    service_type = vars(ServiceType)
    body_response = {}
    body_response["data"] = service_type["_member_names_"]
    return body_response, 200
