# 📄 app/resources/animal_resource.py
from flask_restx import Namespace, Resource
from app.models.animal_record import AnimalRecord
from app.models.camera import Camera, CameraType
from app.models.camera_roi import CameraROI
from app.schemas.animal_schema import AnimalRecordSchema
from datetime import datetime

ns = Namespace('AnimalRecords', description='Детекция животных')
schema = AnimalRecordSchema()
schema_many = AnimalRecordSchema(many=True)

@ns.route('/cameras')
class AnimalCameras(Resource):
    def get(self):
        cams = Camera.query.filter_by(type=CameraType.ANIMAL_CLASSIFIER).all()
        return [{'id': c.id, 'name': c.name} for c in cams]

@ns.route('/cameras/<int:camera_id>')
class AnimalByCamera(Resource):
    def get(self, camera_id):
        from_date = datetime.strptime(ns.payload.get('from_date'), '%Y-%m-%d')
        to_date = datetime.strptime(ns.payload.get('to_date'), '%Y-%m-%d')
        animal_type = ns.payload.get('animal_type')
        records = AnimalRecord.query.join(CameraROI).filter(
            CameraROI.camera_id == camera_id,
            AnimalRecord.created_at >= from_date,
            AnimalRecord.created_at <= to_date,
            AnimalRecord.animal_type == animal_type
        ).all()
        return schema_many.dump(records)

@ns.route('/cameras/<int:camera_id>/hourly')
class AnimalHourly(Resource):
    def get(self, camera_id):
        date = datetime.strptime(ns.payload.get('date'), '%Y-%m-%d')
        animal_type = ns.payload.get('animal_type')
        next_day = date.replace(hour=23, minute=59, second=59)
        records = AnimalRecord.query.join(CameraROI).filter(
            CameraROI.camera_id == camera_id,
            AnimalRecord.created_at >= date,
            AnimalRecord.created_at <= next_day,
            AnimalRecord.animal_type == animal_type
        ).all()
        return schema_many.dump(records)
# animal_resource.py
