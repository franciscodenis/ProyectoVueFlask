from flask import render_template
from src.core import board
from flask import Blueprint
##from src.web.templates.instituciones import index

instituciones_bp = Blueprint("instituciones", __name__, url_prefix="/consultas_instituciones")

@instituciones_bp.get("/")
def index():
    instituciones = board.list_instituciones()
    return render_template("instituciones/index.html",instituciones=instituciones)

def show():
    pass


def new():
    pass


def create():
    pass


def edit():
    pass


def delete():
    pass