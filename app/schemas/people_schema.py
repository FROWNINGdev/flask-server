# 📄 app/schemas/people_schema.py
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.people_record import PeopleRecord

class PeopleRecordSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PeopleRecord
        load_instance = True