# 📄 app/resources/rasta_resource.py
from flask_restx import Namespace, Resource
from app.models.rasta_record import RastaRecord
from app.models.camera import Camera, CameraType
from app.schemas.rasta_schema import RastaRecordSchema
from datetime import datetime

ns = Namespace('RastaRecords', description='Rasta подсчет')
schema = RastaRecordSchema()
schema_many = RastaRecordSchema(many=True)

@ns.route('/cameras')
class RastaCameras(Resource):
    def get(self):
        cams = Camera.query.filter_by(type=CameraType.RASTA).all()
        return [{'id': c.id, 'name': c.name} for c in cams]

@ns.route('/cameras/<int:camera_id>')
class RastaByCamera(Resource):
    def get(self, camera_id):
        from_date = datetime.strptime(ns.payload.get('from_date'), '%Y-%m-%d')
        to_date = datetime.strptime(ns.payload.get('to_date'), '%Y-%m-%d')
        records = RastaRecord.query.join(CameraROI).filter(
            CameraROI.camera_id == camera_id,
            RastaRecord.created_at >= from_date,
            RastaRecord.created_at <= to_date
        ).all()
        return schema_many.dump(records)

@ns.route('/cameras/<int:camera_id>/hourly')
class RastaHourly(Resource):
    def get(self, camera_id):
        date = datetime.strptime(ns.payload.get('date'), '%Y-%m-%d')
        next_day = date.replace(hour=23, minute=59, second=59)
        records = RastaRecord.query.join(CameraROI).filter(
            CameraROI.camera_id == camera_id,
            RastaRecord.created_at >= date,
            RastaRecord.created_at <= next_day
        ).all()
        return schema_many.dump(records)
# rasta_resource.py
