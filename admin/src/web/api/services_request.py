from flask import Blueprint
from src.core import service_requests
from flask import request
from src.web.schemas.services_request import service_requests_schema,create_service_request_schema
from src.core.configuration import get_items_per_page
from flask import jsonify


api_request_bp = Blueprint("request_api", __name__, url_prefix="/api/me")

@api_request_bp.get("/requests")
def request_index():
    """
    Permite acceder al index(listado) del módulo de solicitudes de servicio
    page(optional): Número de página actual.
    per_page(optional): Cantidad de elementos por página.
    """
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', get_items_per_page()))
    except ValueError:
        return jsonify({'error': 'Invalid parameters'}), 400
    if page < 1 or per_page < 1:
        return jsonify({'error': 'Invalid parameters'}), 400
    
    list_request = service_requests.list_service_request()

    # Calcular los índices para la paginación
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    data = service_requests_schema.dump(list_request[start_index:end_index])
    print(type(data))
    return data,200

@api_request_bp.get("/requests/<int:id>")
def request_show(id):
    """
    Obtiene una solicitud de servicio por su ID.
    """
    request_data = service_requests.get_service_request(id)
    
    if request_data is None:
        return jsonify({'error': 'Request not found'}), 404

    return jsonify(request_data), 200

@api_request_bp.post("/requests")
def request_create():
    """
    Crea una nueva solicitud de servicio por un usuario autenticado.
    """
    params = request.get_json()
    errors = create_service_request_schema.validate(params)

    if errors:
        return jsonify({'error': 'Invalid request data', 'details': errors}), 400

    new_request = service_requests.create_service_request(**params)
    return jsonify(new_request), 201

@api_request_bp.put("/requests/<int:id>/notes")
def request_update_notes(id):
    """
    Actualiza las notas de una solicitud por su ID.
    """
    new_data = request.get_json()
    updated_request = service_requests.update_service_request_notes(id, new_data)
    return jsonify(updated_request), 201
