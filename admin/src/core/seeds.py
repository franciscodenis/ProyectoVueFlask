from src.core import auth
from src.core import services
from src.core import institutions

def run():
    admin = auth.create_user(
        email="admin@test.com",
        username="admin",
        password="1234",
        active=True,
        first_name="System",
        last_name="Admin"
    )

    user2 = auth.create_user(
        email="user@test.com",
        username="user",
        password="1234",
        active=True,
        first_name="System",
        last_name="User"
    )
    """
    servicio = services.create_service(
        name="Consulta de servicios",
        description="Permite consultar los servicios",
        keywords="servicios, consultas",
        service_type="ANALISIS",
        enabled=True
    )"""

    institucion1 = institutions.create_institution(
    name="institucion1",
    information="informacion institución 1",
    address="dirección institución 1",
    location="localización institución 1",
    web="www.webinstitucion1.com",
    keywords='["uno","1","primero"]',
    opening_hours="Lun a Vier de 7 a 19",
    contact="institución1@hotmail.com",
    has_authorization=True,
    )
    institucion2 = institutions.create_institution(
    name="institucion2",
    information="informacion institución 2",
    address="dirección institución 2",
    location="localización institución 2",
    web="www.webinstitucion1.com",
    keywords='["dos","2","segundo"]',
    opening_hours="Lun a Vier de 7 a 19",
    contact="institución2@hotmail.com",
    has_authorization=False,
    )