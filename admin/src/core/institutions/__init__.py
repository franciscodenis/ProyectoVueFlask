from src.core.database import db
from src.core.institutions.institution import Institution
from src.core.bcrypt import bcrypt

def list_institutions():
    institution = Institution.query.all()
    return institution


def create_institution(**kwargs):
    ##hash = bcrypt.generate_password_hash(kwargs["password"].encode("utf-8"))
    ##kwargs.update(password=hash.decode("utf-8"))
    institution = Institution(**kwargs)
    db.session.add(institution)
    db.session.commit()

    return institution

"""
def find_user_by_email(email):
    return User.query.filter_by(email=email).first()


def check_user(email, password):
    user = find_user_by_email(email)

    if user and bcrypt.check_password_hash(user.password, password.encode("utf-8")):
        return user
    else:
        return None
"""