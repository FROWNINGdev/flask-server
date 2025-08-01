# 📄 app/schemas/animal_schema.py
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.animal_record import AnimalRecord

class AnimalRecordSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AnimalRecord
        load_instance = True
# animal_schema.py
