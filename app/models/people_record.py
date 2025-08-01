# 📄 app/models/people_record.py
from app.database import db
from sqlalchemy import Enum as PgEnum
import enum


class ActionType(enum.Enum):
    ENTER = 'ENTER'
    EXIT = 'EXIT'


class PeopleRecord(db.Model):
    __tablename__ = 'people_record'
    id = db.Column(db.Integer, primary_key=True)
    camera_id = db.Column(db.Integer, db.ForeignKey('camera.id'), nullable=False)
    action = db.Column(PgEnum(ActionType), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
# people_record.py
