from datetime import datetime
from src.core.database import db

role_has_permissions = db.Table("role_has_permissions",
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
    db.Column("permission_id", db.Integer, db.ForeignKey("permissions.id"), primary_key=True),
)

user_has_roles = db.Table("user_has_roles",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("institution_id", db.Integer, db.ForeignKey("institutions.id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
)

user_has_system_roles = db.Table("user_has_system_roles",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True)
)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    roles = db.relationship("Role", secondary=user_has_roles, lazy='dynamic',
                            backref=db.backref("users", lazy=True))
    system_roles = db.relationship("Role", secondary=user_has_system_roles, lazy=True,
                            backref=db.backref("sys_users", lazy=True))
    institutions = db.relationship("Institution", secondary=user_has_roles, viewonly=True,
                            backref=db.backref("users", lazy=True))
    service_requests = db.relationship("ServiceRequest", back_populates="user", lazy=True)

class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=True)

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=True)
    permissions = db.relationship('Permission', secondary=role_has_permissions, lazy='subquery',
                                  backref=db.backref('roles', lazy=True))

