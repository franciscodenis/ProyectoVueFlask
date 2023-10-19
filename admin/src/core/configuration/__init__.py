from src.core.database import db
from src.core.configuration.configuration import Configuration

def get_or_create_config():
    """
    Permite obtener la configuración o crearla si no existe
    """
    config = Configuration.query.first()
    
    if not config:
        config = Configuration(
            items_per_page=10,
            contact_info='',
            maintenance_mode=False,
            maintenance_message=''
        )
        db.session.add(config)
        db.session.commit()
    
    return config
    
def update_config(new_data):
    """
    Permite actualizar la configuración
    """
    config = Configuration.query.first()
    
    if config:
        config.items_per_page = new_data.get('items_per_page', config.items_per_page)
        config.contact_info = new_data.get('contact_info', config.contact_info)
        config.maintenance_mode = new_data.get('maintenance_mode', config.maintenance_mode)
        config.maintenance_message = new_data.get('maintenance_message', config.maintenance_message)
        
        db.session.commit()
        return config
    else:
        print("Configuración no encontrada.")
        return None
    
def get_items_per_page():
    """
    Permite obtener la cantidad de items por página. Por default devuelve 10
    """
    config = get_or_create_config()
    
    if config:
        return config.items_per_page
    else:
        return 10
