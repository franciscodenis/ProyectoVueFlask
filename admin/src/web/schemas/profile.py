from marshmallow import Schema, fields
from src.core.auth.user import User

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    username = fields.Str()
    active = fields.Bool()

user_schema = UserSchema()
