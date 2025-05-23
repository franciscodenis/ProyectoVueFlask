from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    """
    Inicialización de la aplicación.
    """

    db.init_app(app)
    config_db(app)


def config_db(app):
    """
    Configuración de la base de datos.
    """

    @app.teardown_request
    def close_session(exception=None):
        db.session.close()


def reset_db():
    """
    Resetea la base de datos.
    """
    print("Eliminando base de datos...")
    db.drop_all()
    print("Creando base de datos...")
    db.create_all()
    print("👍Listo...")
