# 📄 app/models/roi.py
from app.database import db
from sqlalchemy import Enum as PgEnum
import enum

class RoiType(enum.Enum):
    RASTA = 'RASTA'
    FOOD = 'FOOD'
    ANIMAL = 'ANIMAL'

class ROI(db.Model):
    __tablename__ = 'roi'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    geometry = db.Column(db.JSON, nullable=False)
    type = db.Column(PgEnum(RoiType), nullable=False)