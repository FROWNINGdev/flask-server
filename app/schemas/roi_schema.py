# 📄 app/schemas/roi_schema.py
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.camera_roi import ROI


class ROISchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ROI
        load_instance = True
# roi_schema.py
