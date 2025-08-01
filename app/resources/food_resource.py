# 📄 app/resources/food_resource.py
from flask_restx import Namespace, Resource
from app.models.food_record import FoodRecord
from app.models.camera import Camera, CameraType
from app.models.camera_roi import CameraROI
from app.schemas.food_schema import FoodRecordSchema
from datetime import datetime

ns = Namespace('FoodRecords', description='Детекция еды')
schema = FoodRecordSchema()
schema_many = FoodRecordSchema(many=True)


@ns.route('/cameras')
class FoodCameras(Resource):
    def get(self):
        cams = Camera.query.filter_by(type=CameraType.FOOD).all()
        return [{'id': c.id, 'name': c.name} for c in cams]


@ns.route('/cameras/<int:camera_id>')
class FoodByCamera(Resource):
    def get(self, camera_id):
        from_date = datetime.strptime(ns.payload.get('from_date'), '%Y-%m-%d')
        to_date = datetime.strptime(ns.payload.get('to_date'), '%Y-%m-%d')
        records = FoodRecord.query.join(CameraROI).filter(
            CameraROI.camera_id == camera_id,
            FoodRecord.created_at >= from_date,
            FoodRecord.created_at <= to_date
        ).all()
        return schema_many.dump(records)


@ns.route('/cameras/<int:camera_id>/hourly')
class FoodHourly(Resource):
    def get(self, camera_id):
        date = datetime.strptime(ns.payload.get('date'), '%Y-%m-%d')
        next_day = date.replace(hour=23, minute=59, second=59)
        records = FoodRecord.query.join(CameraROI).filter(
            CameraROI.camera_id == camera_id,
            FoodRecord.created_at >= date,
            FoodRecord.created_at <= next_day
        ).all()
        return schema_many.dump(records)
# food_resource.py
