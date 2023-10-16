from src.core.database import db
from src.core.auth.user import User
from src.core.auth.user import Permission
from src.core.auth.user import Role
from src.core.auth.user import role_has_permissions
from src.core.auth.user import user_has_roles
from src.core.bcrypt import bcrypt

def list_users():
    users = User.query.all()

    return users


def create_user(**kwargs):
    hash = bcrypt.generate_password_hash(kwargs["password"].encode("utf-8"))
    kwargs.update(password=hash.decode("utf-8"))
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()

    return user

def find_user_by_email(email):
    return User.query.filter_by(email=email).first()


def check_user(email, password):
    user = find_user_by_email(email)

    if user and bcrypt.check_password_hash(user.password, password.encode("utf-8")):
        return user
    else:
        return None


def list_permissions():
    permissions = Permission.query.all()

    return permissions

def create_permission(**kwargs):
    permission = Permission(**kwargs)
    db.session.add(permission)
    db.session.commit()

    print(f"Permission: {permission.name} id: {permission.id}")
    return permission

def list_permissions_by_user_id(user_id):

    # !! db.session.execute(db.select(Permission, Role).join_from(Permission, Permission.roles)).all()
    # !! db.session.execute(db.select(Permission, Role).join_from(Permission, Permission.roles).filter(Role.id==1)).all()
    # !! subq = (db.session.query(Role).join(User, Role.users).filter(User.id == 1)).subquery("subq")
    # !! db.session.execute(db.select(Permission, Role).join_from(Permission, Permission.roles).filter(Role.id.in_(db.session.query(Role.id).join(User, Role.users).filter(User.id == 1)))).all()
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
        ).scalars().all()

    # j = role_has_permissions.join(user_has_roles, role_has_permissions.c.role_id == user_has_roles.c.role_id)
    # statement = db.select(role_has_permissions).select_from(j).where(user_has_roles.c.user_id == user_id)
    # print(statement)

    # j = user_has_roles.join(role_has_permissions, user_has_roles.c.role_id == role_has_permissions.c.role_id)

    # print("TEST")
    # statement = select(user_has_roles).select_from(j).where(user_has_roles.c.user_id == user_id)



def list_roles():
    roles = Role.query.all()

    return roles

def create_role(**kwargs):
    role = Role(**kwargs)
    db.session.add(role)
    db.session.commit()

    return role

def set_role_permissions(role, permissions):
    role_id = role.id
    for permission in permissions:
        print(f"Role [{role.id} : {role.name}] - Permission [{permission.id} : {permission.name}]")
        statement = role_has_permissions.insert().values(role_id=role_id, permission_id=permission.id)
        db.session.execute(statement)
    db.session.commit()

def set_user_roles(user, roles):
    user_id = user.id
    for role in roles:
        print (f"User [{user.id} : {user.username}] - Role [{role.id} : {role.name}]")
        statement = user_has_roles.insert().values(user_id=user_id, role_id=role.id)
        db.session.execute(statement)
    db.session.commit()