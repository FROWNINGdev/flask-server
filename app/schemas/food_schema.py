# 📄 app/schemas/food_schema.py
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.food_record import FoodRecord

class FoodRecordSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FoodRecord
        load_instance = True
# food_schema.py
