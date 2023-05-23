from marshmallow import fields

from app.extensions import marshmallow

class CourseSchema(marshmallow.Schema):
    id = fields.Integer(dump_only=True)
    professor = fields.String()
    title = fields.String()
    description = fields.String()
    url = fields.String()
