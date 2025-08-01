# 📄 app/models/animal_record.py
from app.database import db
from sqlalchemy import Enum as PgEnum
import enum

class ActionType(enum.Enum):
    ENTER = 'ENTER'
    EXIT = 'EXIT'

class AnimalRecord(db.Model):
    __tablename__ = 'animal_record'
    id = db.Column(db.Integer, primary_key=True)
    cameraRoiId = db.Column(db.Integer, db.ForeignKey('camera_roi.id'), nullable=False)
    action = db.Column(PgEnum(ActionType), nullable=False)
    animal_type = db.Column(db.String(100), nullable=False)
    photo_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False)
# animal_record.py
