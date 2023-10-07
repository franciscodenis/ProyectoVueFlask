from flask import render_template
from src.core import services
from flask import Blueprint

services_bp = Blueprint("servicios", __name__, url_prefix="/consultas_servicios")

@services_bp.get("/")
def service_index():
    """
    Permite accede al index(listado) del módulo de servicios
    """
    servicios = services.list_services()
    return render_template("services/index.html",servicios=servicios)
