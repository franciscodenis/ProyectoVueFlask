from src.core import auth
from src.core import services
from src.core import institutions
from src.core import configuration

def run():
    # Institutions
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

    # Permissions
    all_permissions = {
        "user_index": auth.create_permission(
            name = "user_index"
        ),
        "user_create": auth.create_permission(
            name = "user_create"
        ),
        "user_destroy": auth.create_permission(
            name = "user_destroy"
        ),
        "user_update": auth.create_permission(
            name = "user_update"
        ),
        "user_show": auth.create_permission(
            name = "user_show"
        ),
        "institution_index": auth.create_permission(
            name = "institution_index"
        ),
        "institution_create": auth.create_permission(
            name = "institution_create"
        ),
        "institution_destroy": auth.create_permission(
            name = "institution_destroy"
        ),
        "institution_update": auth.create_permission(
            name = "institution_update"
        ),
        "institution_show": auth.create_permission(
            name = "institution_show"
        ),
        "member_index": auth.create_permission(
            name = "member_index"
        ),
        "member_create": auth.create_permission(
            name = "member_create"
        ),
        "member_destroy": auth.create_permission(
            name = "member_destroy"
        ),
        "member_update": auth.create_permission(
            name = "member_update"
        ),
        # TODO: Revisar si es necesaria
        "member_show": auth.create_permission(
            name = "member_show"
        ),
        "service_index": auth.create_permission(
            name = "service_index"
        ),
        "service_create": auth.create_permission(
            name = "service_create"
        ),
        "service_destroy": auth.create_permission(
            name = "service_destroy"
        ),
        "service_update": auth.create_permission(
            name = "service_update"
        ),
        "service_show": auth.create_permission(
            name = "service_show"
        ),
        "request_index": auth.create_permission(
            name = "request_index"
        ),
        # TODO: Revisar si es necesaria
        "request_create": auth.create_permission(
            name = "request_create"
        ),
        "request_destroy": auth.create_permission(
            name = "request_destroy"
        ),
        "request_update": auth.create_permission(
            name = "request_update"
        ),
        "request_show": auth.create_permission(
            name = "request_show"
        ),
        "config_show": auth.create_permission(
            name = "config_show"
        ),
        "config_update": auth.create_permission(
            name = "config_update"
        ),
    }

    # Roles
    super_admin_role = auth.create_role(
        name = "Super Administrador"
    )

    owner_role = auth.create_role(
        name = "Dueño"
    )

    admin_role = auth.create_role(
        name = "Administrador"
    )

    operator_role = auth.create_role(
        name = "Operador"
    )

    # Users
    super_admin = auth.create_user(
        email="admin@test.com",
        username="superadmin",
        password="1234",
        active=True,
        first_name="Super",
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

    # Role has permissions
    super_admin_role_permissions = [
        *all_permissions.values()
    ]

    owner_role_permissions = [
        all_permissions["member_index"],
        all_permissions["member_create"],
        all_permissions["member_destroy"],
        all_permissions["member_update"],
        all_permissions["member_show"],
        all_permissions["service_index"],
        all_permissions["service_show"],
        all_permissions["service_update"],
        all_permissions["service_create"],
        all_permissions["service_destroy"],
        all_permissions["request_index"],
        all_permissions["request_show"],
        all_permissions["request_update"],
        all_permissions["request_destroy"],
    ]

    admin_role_permissions = [
        all_permissions["service_index"],
        all_permissions["service_show"],
        all_permissions["service_update"],
        all_permissions["service_create"],
        all_permissions["service_destroy"],
        all_permissions["request_index"],
        all_permissions["request_show"],
        all_permissions["request_update"],
        all_permissions["request_destroy"],
    ]

    operator_role_permissinos = [
        all_permissions["service_index"],
        all_permissions["service_show"],
        all_permissions["service_update"],
        all_permissions["service_create"],
        all_permissions["request_index"],
        all_permissions["request_show"],
        all_permissions["request_update"],
    ]

    auth.set_role_permissions(super_admin_role, super_admin_role_permissions)
    auth.set_role_permissions(owner_role, owner_role_permissions)
    auth.set_role_permissions(admin_role, admin_role_permissions)
    auth.set_role_permissions(operator_role, operator_role_permissinos)

    # User has roles
    auth.set_user_roles(super_admin, institucion1.id, [super_admin_role.id])
    auth.set_user_roles(super_admin, institucion2.id, [super_admin_role.id])

    # User has system roles
    auth.set_user_system_roles(super_admin, [super_admin_role.id])

    servicio = services.create_service(
        name="Consulta de servicios",
        description="Permite consultar los servicios",
        keywords="servicios, consultas",
        service_type="ANALISIS",
        enabled=True
    )


    config = configuration.get_or_create_config()
