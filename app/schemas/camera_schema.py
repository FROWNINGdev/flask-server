from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, validate
from app.models.camera import Camera, CameraType

class CameraSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Camera
        load_instance = True

    # Переопределим поле 'type' вручную как строку
    type = fields.String(
        required=True,
        validate=validate.OneOf([t.name for t in CameraType])  # Enum name
    )