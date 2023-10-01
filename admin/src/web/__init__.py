from flask import Flask
from flask import render_template
from src.web import error
from src.web.controllers.instituciones import instituciones_bp
from src.web.config import config

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)

    app.register_blueprint(instituciones_bp)
    app.config.from_object(config[env])

    @app.get("/")
    def home():
        return render_template("home.html")

    app.register_error_handler(404, error.not_found_error)

    return app
