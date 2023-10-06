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