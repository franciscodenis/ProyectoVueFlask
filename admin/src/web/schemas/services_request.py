from marshmallow import Schema, fields

class ServiceRequestSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    service_id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    notes = fields.Str()
    status = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class CreateServiceRequestSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)

service_request_schema = ServiceRequestSchema()
service_requests_schema = ServiceRequestSchema(many=True)
create_service_request_schema = CreateServiceRequestSchema()