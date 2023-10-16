from src.core.database import db
from src.core.configuration.configuration import Configuration

def get_or_create_config():
    """
    Permite obtener la configuración o crearla si no existe
    """
    try:
        config = Configuration.query.first()
        if config:
            return config
        else:
            config = Configuration(
                items_per_page=10,
                contact_info='',
                maintenance_mode=False,
                maintenance_message=''
            )
            db.session.add(config)
            db.session.commit()
            return config
    except Exception as e:
        print(f"Error al obtener la configuración: {str(e)}")
        return None
    
def update_config(new_data):
    """
    Permite actualizar la configuración
    """
    try:
        config = Configuration.query.first()
        if config:
            config.items_per_page = new_data['items_per_page']
            config.contact_info = new_data['contact_info']
            config.maintenance_mode = new_data['maintenance_mode']
            config.maintenance_message = new_data['maintenance_message']
            db.session.add(config)
            db.session.commit()
            return config
        else:
            print("Configuración no encontrada.")
            return None
    except Exception as e:
        print(f"Error al actualizar la configuración: {str(e)}")
        return None