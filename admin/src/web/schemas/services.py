from marshmallow import Schema, fields


class ServiceSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    keywords = fields.Str()
    service_type = fields.Str()
    enabled = fields.Bool()


service_schema = ServiceSchema()
service_schemas = ServiceSchema(many=True)


class ServiceTypeSchema(Schema):
    name = fields.Str()


service_type_schema = ServiceTypeSchema()
service_type_schemas = ServiceTypeSchema(many=True)
