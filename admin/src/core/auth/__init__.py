from os import environ
from src.core.database import db
from src.core.auth.user import User
from src.core.auth.user import Permission
from src.core.auth.user import Role
from src.core.auth.user import role_has_permissions
from src.core.auth.user import user_has_roles
from src.core.institutions.institution import Institution
from src.core.bcrypt import bcrypt
from src.core.email import mail
from flask_mail import Message

def list_users():
    """
    Lista todos los usuarios
    """
    users = User.query.all()

    return users

def create_user_stub(email, first_name, last_name):
    """
    Crea un stub de usuario inactivo y envía email de activación
    """
    user = find_user_by_email(email)

    if user:
        return None

    user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            active=False
        )
    db.session.add(user)
    db.session.commit()

    key = bcrypt.generate_password_hash(email.encode("utf-8"))
    decoded_key = key.decode("utf-8")

    base_url = environ.get("APP_BASE_URL", "https://admin-grupo32.proyecto2023.linti.unlp.edu.ar")
    link = f"{base_url}/auth/validate?email={email}&key={decoded_key}"

    msg = Message(
        subject="Activar usuario CIDEPINT",
        recipients=[email],
        body=f"La dirección {email} ha sido utilizada recientemente para registrar un usuario en CIDEPINT Admin. Para activarlo usa el siguiente link en tu navegador: {link}"
        )
    mail.send(msg)

    return user

def create_user(**kwargs):
    """
    Crea un nuevo usuario
    """
    hash = bcrypt.generate_password_hash(kwargs["password"].encode("utf-8"))
    kwargs.update(password=hash.decode("utf-8"))
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()

    return user

def find_user_by_email(email):
    """
    Obtiene un usuario por email
    """
    return User.query.filter_by(email=email).first()

def get_user_by_id(user_id):
    """
    Obtiene un usuario por id
    """
    return User.query.get(user_id)

def check_user(email, password):
    """
    Valida email y contraseña de usuario
    """
    user = find_user_by_email(email)

    if user and bcrypt.check_password_hash(user.password, password.encode("utf-8")):
        return user
    else:
        return None

def validate_email(email, key):
    """
    Valida email contra la key de activación
    """
    if bcrypt.check_password_hash(key, email.encode("utf-8")):
        user = find_user_by_email(email)
        if not user.active and not user.password:
            return True

    return False

def activate_user(email, username, password):
    """
    Activa un usuario y configura username y password
    """
    hash = bcrypt.generate_password_hash(password.encode("utf-8"))
    user = find_user_by_email(email)
    if not user.active and not user.password:
        user.active = True
        user.username = username
        user.password = hash.decode("utf-8")
        db.session.add(user)
        db.session.commit()

        return user

    return None


def list_permissions():
    """
    Obtiene una lista de permisos
    """
    permissions = Permission.query.all()

    return permissions

def create_permission(**kwargs):
    """
    Crea un nuevo permiso
    """
    permission = Permission(**kwargs)
    db.session.add(permission)
    db.session.commit()

    print(f"Permission: {permission.name} id: {permission.id}")
    return permission

def list_permissions_by_user_id(user_id):
    """
    Obtiene una lista de nombres de permisos para un usuario por id
    """
    return db.session.execute(
        db.select(Permission.name.distinct())
        .join_from(Permission, Permission.roles)
        .filter(
            Role.id.in_(
                db.select(Role.id)
                .join(User, Role.users)
                .filter(User.id == user_id)
                )
            )
        ).scalars().all()

def list_permissions_by_user_id_and_institution_id(user_id, institution_id):
    """
    Obtiene una lista de nombres de permisos por ids de usuario e institución
    """
    return db.session.execute(
        db.select(Permission.name)
        .join_from(Permission, Permission.roles)
        .filter(
            Role.id.in_(
                db.select(Role.id)
                .join(User, Role.users)
                .filter(User.id == user_id)
                )
            )
        .filter(
            Institution.id == institution_id
        )
        ).scalars().all()

def list_roles():
    """
    Obtiene una lista de roles
    """
    roles = Role.query.all()

    return roles

def create_role(**kwargs):
    """
    Crea un nuevo rol
    """
    role = Role(**kwargs)
    db.session.add(role)
    db.session.commit()

    return role

def set_role_permissions(role, permissions):
    """
    Asigna permisos a un rol
    """
    role_id = role.id
    for permission in permissions:
        print(f"Role [{role.id} : {role.name}] - Permission [{permission.id} : {permission.name}]")
        statement = role_has_permissions.insert().values(role_id=role_id, permission_id=permission.id)
        db.session.execute(statement)
    db.session.commit()

def set_user_roles(user, institution, roles):
    """
    Asigna roles a un usuario en una institución
    """
    user_id = user.id
    institution_id = institution.id
    for role in roles:
        print (f"User [{user.id} : {user.username}] - Institution [{institution.id} : {institution.name}] - Role [{role.id} : {role.name}]")
        statement = user_has_roles.insert().values(user_id=user_id, institution_id=institution_id, role_id=role.id)
        db.session.execute(statement)
    db.session.commit()

def update_user(user_id, new_data):
    """
    Actualiza un usuario
    """
    try:
        usuario = User.query.get(user_id)
        if usuario:
            usuario.first_name = new_data["first_name"]
            usuario.last_name = new_data["last_name"]
            usuario.username = new_data["username"]
            usuario.active = new_data["active"]

            db.session.add(usuario)
            db.session.commit()
            return usuario
    except Exception as e:
        print(f"Error al actualizar el usuario: {str(e)}")
        return None


def delete_user(user_id):
    """
    Elimina un usuario
    """
    try:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar el usuario: {str(e)}")
        return None
