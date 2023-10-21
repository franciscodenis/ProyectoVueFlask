from src.core.database import db
from src.core.service_requests.service_request import ServiceRequest
from src.core.services.service import Service
from src.core.configuration import get_items_per_page


def list_service_request(
    page, service_type=None, start_date=None, end_date=None, state=None, user_id=None
):
    """
    Permite listar las solicitudes de servicio de forma paginada y filtrada
    """
    # Realiza la consulta de acuerdo a los parámetros de filtro
    query = ServiceRequest.query

    if service_type:
        query = query.filter(ServiceRequest.service.has(ServiceType=service_type))

    if start_date:
        query = query.filter(ServiceRequest.created_at >= start_date)

    if end_date:
        query = query.filter(ServiceRequest.created_at <= end_date)

    if state:
        query = query.filter(ServiceRequest.state == state)

    if user_id:
        query = query.filter(ServiceRequest.user_id == user_id)

    # Pagina los resultados
    pagination = query.paginate(
        page=page, per_page=get_items_per_page(), error_out=False
    )

    return pagination

def list_service_request_by_institution_id(
    institution_id, page, service_type=None, start_date=None, end_date=None, state=None, user_id=None
):
    """
    Permite listar las solicitudes de servicio de forma paginada y filtrada
    """
    # Realiza la consulta de acuerdo a los parámetros de filtro
    query = ServiceRequest.query.filter(ServiceRequest.service.has(Service.institution_id == institution_id))

    if service_type:
        query = query.filter(ServiceRequest.service.has(ServiceType=service_type))

    if start_date:
        query = query.filter(ServiceRequest.created_at >= start_date)

    if end_date:
        query = query.filter(ServiceRequest.created_at <= end_date)

    if state:
        query = query.filter(ServiceRequest.state == state)

    if user_id:
        query = query.filter(ServiceRequest.user_id == user_id)

    # Pagina los resultados
    pagination = query.paginate(
        page=page, per_page=get_items_per_page(), error_out=False
    )

    return pagination


def get_service_request(id):
    """
    Permite obtener una solicitud de servicio por su id
    """
    try:
        request = ServiceRequest.query.get(id)
        return request
    except Exception as e:
        print(f"Error al obtener la solicitud: {str(e)}")
        return None


def create_service_request(**kwargs):
    """
    Permite crear una solicitud de servicio
    """
    try:
        new_request = ServiceRequest(**kwargs)
        db.session.add(new_request)
        db.session.commit()
        return new_request
    except Exception as e:
        print(f"Error al crear la solicitud: {str(e)}")
        return None


def update_service_request(id, new_data):
    """
    Permite actualizar una solicitud de servicio
    """
    try:
        request = ServiceRequest.query.get(id)
        if request:
            request.title = new_data["title"]
            request.description = new_data["description"]
            request.status = new_data["status"]
            request.notes = new_data["notes"]
            db.session.add(request)
            db.session.commit()
            return request
        else:
            print("Solicitud no encontrada.")
            return None
    except Exception as e:
        print(f"Error al actualizar la solicitud: {str(e)}")
        return None


def delete_service_request(id):
    """
    Permite eliminar una solicitud de servicio
    """
    try:
        request = ServiceRequest.query.get(id)
        db.session.delete(request)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar la solicitud: {str(e)}")
        return None
