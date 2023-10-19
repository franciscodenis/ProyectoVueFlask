from marshmallow import Schema, fields
from src.core import institutions

class InstitutionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    information = fields.Str()
    address = fields.Str()
    location = fields.Str()
    web = fields.Str()
    keywords = fields.Str()
    opening_hours = fields.Str()
    contact = fields.Str()
    has_authorization = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

institution_schema = InstitutionSchema()
institutions_schema =InstitutionSchema(many=True)

