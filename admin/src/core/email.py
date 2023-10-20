from flask_mail import Mail
from os import environ

mail = Mail()

def init_app(app):
    """
    Inicialización de la aplicación.
    """

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USERNAME"] = environ.get("APP_EMAIL_ADDRESS", "proyecto2023grupo32@gmail.com")
    app.config["MAIL_DEFAULT_SENDER"] = environ.get("APP_EMAIL_ADDRESS", "proyecto2023grupo32@gmail.com")
    app.config["MAIL_PASSWORD"] = environ.get("APP_EMAIL_PASSWORD", "ikbv ycvc qwbd anha")
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True
    mail.init_app(app)

