# 📄 app/schemas/rasta_schema.py
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.rasta_record import RastaRecord


class RastaRecordSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RastaRecord
        load_instance = True
# rasta_schema.py
