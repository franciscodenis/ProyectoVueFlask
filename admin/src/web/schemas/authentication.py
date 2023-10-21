from marshmallow import Schema, fields
from src.core.auth import user


class UserSchema(Schema):
    user = fields.Email(required=True)
    password = fields.Str(required=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
