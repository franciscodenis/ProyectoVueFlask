from src.core.database import db
from src.core.institutions.institution import Institution
from src.core.bcrypt import bcrypt
from src.core.configuration import get_items_per_page

def list_institutions(page):
    """
    Permite listar institutciones de forma paginada
    """
    return Institution.query.paginate(
        page=page, per_page=get_items_per_page(), error_out=False
    )


def create_institution(**new_data):
    """
    Permite crear un servicio
    """
    try:
        institution = Institution(**new_data)
        db.session.add(institution)
        db.session.commit()
        return institution
    except Exception as e:
        print(f"Error al crear el servicio: {str(e)}")
        return None
    
def create_institution(new_data):
    """
    Permite crear un servicio
    """
    try:
        institution = Institution(**new_data)
        db.session.add(institution)
        db.session.commit()
        return institution
    except Exception as e:
        print(f"Error al crear el servicio: {str(e)}")
        return None


def get_institution_by_id(institution_id):
    """
    Permite obtener un servicio por id
    """
    return Institution.query.get(institution_id)

def update_institution(institution_id, new_data):
    """
    Permite actualizar un servicio
    """
    try:
        institution = Institution.query.get(institution_id)
        if institution:
            institution.name = new_data['name']
            institution.information = new_data['information']
            institution.address = new_data['address']
            institution.location = new_data['location']
            institution.web = new_data['web']
            institution.keywords = new_data['keywords']
            institution.opening_hours = new_data['opening_hours']
            institution.contact = new_data['contact']
            institution.has_authorization = new_data['has_authorization']

            db.session.add(institution)
            db.session.commit()
            return institution
        else:
            print("Institucion no encontrada.")
            return None
    except Exception as e:
        print(f"Error al actualizar la institucion: {str(e)}")
        return None

def delete_institution(institution_id):
    """
    Permite eliminar un servicio
    """
    try:
        institution = Institution.query.get(institution_id)
        db.session.delete(institution)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar el servicio: {str(e)}")
        return None
