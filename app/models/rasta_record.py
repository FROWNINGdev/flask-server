# 📄 app/models/rasta_record.py
from app.database import db


class RastaRecord(db.Model):
    __tablename__ = 'rasta_record'
    id = db.Column(db.Integer, primary_key=True)
    cameraRoiId = db.Column(db.Integer, db.ForeignKey('camera_roi.id'), nullable=False)
    peopleCount = db.Column(db.Integer, nullable=False)
    photo_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False)
# rasta_record.py
