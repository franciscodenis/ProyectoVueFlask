from flask import Flask
from flask import render_template
from flask_session import Session
from src.core import database
from src.core import seeds
from src.web import error
from src.web.config import config
from src.web import routes
from src.core.bcrypt import bcrypt
from src.web.helpers import auth

session = Session()

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    session.init_app(app)
    database.init_app(app)
    bcrypt.init_app(app)

    routes.register(app)

    @app.get("/")
    def home():
        return render_template("home.html")

    app.register_error_handler(404, error.not_found_error)
    app.register_error_handler(401, error.unauthorized)

    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seedsdb")
    def seedsdb():
        seeds.run()

    return app
