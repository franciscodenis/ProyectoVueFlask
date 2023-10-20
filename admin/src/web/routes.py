from src.web.controllers.users import user_bp
from src.web.controllers.auth import auth_bp
from src.web.controllers.institutions import instituciones_bp
from src.web.controllers.services import services_bp
from src.web.api.institutions import api_instituciones_bp
from src.web.api.authentication import api_authentication_bp
from src.web.api.services_request import api_request_bp
from src.web.controllers.configuration import configuration_bp
from src.web.controllers.members import members_bp
from src.web.controllers.services_request import service_requests_bp

def register(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(instituciones_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(api_instituciones_bp)
    app.register_blueprint(configuration_bp)
    app.register_blueprint(api_authentication_bp)
    app.register_blueprint(api_request_bp)
    app.register_blueprint(members_bp)
    app.register_blueprint(service_requests_bp)
