from src.core.services.service import Service
from src.core.database import db

def list_services():
    """
    Permite listar los servicios
    """
    return Service.query.all()

def create_service(**kwargs):
    """
    Permite crear un servicio
    """
    try:
        service = Service(**kwargs)
        db.session.add(service)
        db.session.commit()
        return service
    except Exception as e:
        print(f"Error al crear el servicio: {str(e)}")
        return None

def get_service_by_id(service_id):
    """
    Permite obtener un servicio por id
    """
    return Service.query.get(service_id)

def update_service(service_id, new_data):
    """
    Permite actualizar un servicio
    """
    try:
        service = Service.query.get(service_id)
        if service:
            service.name = new_data['name']
            service.description = new_data['description']
            service.keywords = new_data['keywords']
            service.service_type = new_data['service_type']
            service.enabled = new_data['enabled']
            db.session.add(service)
            db.session.commit()
            return service
        else:
            print("Servicio no encontrado.")
            return None
    except Exception as e:
        print(f"Error al actualizar el servicio: {str(e)}")
        return None