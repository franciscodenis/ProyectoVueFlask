from flask import render_template


def not_found_error(e):
    """
    devuelve un mensaje de error 404
    """
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que se quiere acceder no existe",
    }

    return render_template("error.html", **kwargs), 404


def unauthorized(e):
    """
    Devuelve un mensaje de error 401
    """
    kwargs = {
        "error_name": "401 Unauthorized",
        "error_description": "No tienes los permisos necesarios para acceder al recurso",
    }

    return render_template("error.html", **kwargs), 401
