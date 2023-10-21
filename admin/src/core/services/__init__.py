from src.core.services.service import Service
from src.core.database import db
from src.core.configuration import get_items_per_page
from src.core.configuration import Configuration


def list_services(page):
    """
    Permite listar los servicios
    """
    return Service.query.paginate(
        page=page, per_page=get_items_per_page(), error_out=False
    )


def list_services_by_institution(institution_id, page):
    """
    Permite listar los servicios
    """
    return Service.query.filter(Service.institution_id == institution_id).paginate(
        page=page, per_page=get_items_per_page(), error_out=False
    )


def list_service_search(search="", type="", page=1, per_page=0):
    if per_page == 0:
        per_page = get_items_per_page()

    if type == "":
        return Service.query.filter(
            (Service.description.like("%" + search + "%"))
            | (Service.name.like("%" + search + "%"))
            | (Service.keywords.like("%" + search + "%"))
        ).paginate(page=page, per_page=per_page)

    return (
        Service.query.filter(
            (Service.description.like("%" + search + "%"))
            | (Service.name.like("%" + search + "%"))
            | (Service.keywords.like("%" + search + "%"))
        )
        .filter((Service.service_type == type))
        .paginate(page=page, per_page=per_page)
    )


def services_count():
    return Service.query.count()


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
            service.name = new_data["name"]
            service.description = new_data["description"]
            service.keywords = new_data["keywords"]
            service.service_type = new_data["service_type"]
            service.enabled = new_data["enabled"]
            db.session.add(service)
            db.session.commit()
            return service
        else:
            print("Servicio no encontrado.")
            return None
    except Exception as e:
        print(f"Error al actualizar el servicio: {str(e)}")
        return None


def delete_service(service_id):
    """
    Permite eliminar un servicio
    """
    try:
        service = Service.query.get(service_id)
        db.session.delete(service)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar el servicio: {str(e)}")
        return None
