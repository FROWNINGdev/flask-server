# 📄 app/models/camera.py
from app.database import db
from sqlalchemy import Enum as PgEnum
import enum

class CameraType(enum.Enum):
    PEOPLE_TRAFFIC_COUNTING = 'PEOPLE_TRAFFIC_COUNTING'
    RASTA = 'RASTA'
    FOOD = 'FOOD'
    ANIMAL_CLASSIFIER = 'ANIMAL_CLASSIFIER'

class Camera(db.Model):
    __tablename__ = 'camera'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ip = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    type = db.Column(PgEnum(CameraType), nullable=False)