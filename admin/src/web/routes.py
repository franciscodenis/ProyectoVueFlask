from src.web.controllers.users import user_bp
from src.web.controllers.auth import auth_bp
from src.web.controllers.institutions import instituciones_bp
from src.web.controllers.services import services_bp

def register(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(instituciones_bp)
    app.register_blueprint(services_bp)