from flask import redirect, url_for, render_template
from src.core import configuration
from src.web.helpers.auth import is_superadmin
from functools import wraps

def superadmin_during_maintenance(view_func):
    def decorated(*args, **kwargs):
        if configuration.is_maintenance_mode_enabled() and not is_superadmin():
            return render_template('maintenance.html')  # Muestra una página de mantenimiento
        return view_func(*args, **kwargs)

    return decorated

def maintenance_mode_guard(view_func):
    @wraps(view_func)
    def decorated(*args, **kwargs):
        if configuration.is_maintenance_mode_enabled():
            return render_template('maintenance.html')  # Muestra una página de mantenimiento
        return view_func(*args, **kwargs)

    return decorated