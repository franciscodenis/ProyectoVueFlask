from src.core.database import db
from src.core.service_requests.service_request import ServiceRequest

def list_service_request():
    """
    Permite listar las solicitudes de servicio
    """
    try:
        list_request = ServiceRequest.query.all()
        return list_request
    except Exception as e:
        print(f"Error al obtener la lista de solicitudes: {str(e)}")
        return None
    
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

def update_service_request_notes(id,new_data):
    """
    Permite actualizar las notas de una solicitud
    """
    try:
        request = ServiceRequest.query.get(id)
        if request:
            request.notes = new_data['notes']
            db.session.add(request)
            db.session.commit()
            return request
        else:
            print("Solicitud no encontrada.")
            return None
    except Exception as e:
        print(f"Error al actualizar la solicitud: {str(e)}")
        return None
