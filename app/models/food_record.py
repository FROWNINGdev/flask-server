# 📄 app/models/food_record.py
from app.database import db

class FoodRecord(db.Model):
    __tablename__ = 'food_record'
    id = db.Column(db.Integer, primary_key=True)
    cameraRoiId = db.Column(db.Integer, db.ForeignKey('camera_roi.id'), nullable=False)
    food_types = db.Column(db.JSON, nullable=False)
    photo_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False)

