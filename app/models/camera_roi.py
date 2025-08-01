# 📄 app/models/camera_roi.py
from app.database import db


# camera_roi.py
class CameraROI(db.Model):
    __tablename__ = 'camera_roi'
    id = db.Column(db.Integer, primary_key=True)
    camera_id = db.Column(db.Integer, db.ForeignKey('camera.id'))
    roi_id = db.Column(db.Integer, db.ForeignKey('camera_rois.id'), nullable=False)  # fix here!
# camera_roi.py
class ROI(db.Model):
    __tablename__ = 'camera_rois'

    id = db.Column(db.Integer, primary_key=True)
    camera_id = db.Column(db.Integer, db.ForeignKey('camera.id'))
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)