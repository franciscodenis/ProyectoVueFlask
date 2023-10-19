from functools import wraps
from flask import session
from flask import abort
from src.core import auth

def is_authenticated(session):
    return session.get("user") is not None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated(session):
            return abort(401)
        return f(*args, **kwargs)

    return decorated_function

def has_permission(required_permissions_list):
    has_permission = True
    user = auth.find_user_by_email(session.get("user"))
    institution = session.get("institution")
    if not institution:
        return False

    user_permissions_list = auth.list_permissions_by_user_id_and_institution_id(user.id, institution)

    for permission in required_permissions_list:
        if not (permission in user_permissions_list):
            has_permission = False
            break

    return has_permission

def has_system_permission(required_system_permissions_list):
    has_permission = True
    user = auth.find_user_by_email(session.get("user"))

    user_system_permissions_list = auth.list_system_permissions_by_user_id(user.id)

    for permission in required_system_permissions_list:
        if not (permission in user_system_permissions_list):
            has_permission = False
            break

    return has_permission
