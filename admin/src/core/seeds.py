from src.core import auth
from src.core import services

def run():
    admin = auth.create_user(
        email="admin@test.com",
        username="admin",
        password="1234",
        active=True,
        first_name="System",
        last_name="Admin"
    )

    servicio = services.create_service(
        name="Consulta de servicios",
        description="Permite consultar los servicios",
        keywords="servicios, consultas",
        service_type="ANALISIS",
        enabled=True
    )