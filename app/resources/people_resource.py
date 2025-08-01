# 📄 app/resources/people_resource.py
from flask_restx import Namespace, Resource
from app.models.people_record import PeopleRecord
from app.models.camera  import Camera, CameraType
from app.schemas.people_schema import PeopleRecordSchema
from datetime import datetime

ns = Namespace('PeopleRecords', description='Учет людей')
schema = PeopleRecordSchema()
schema_many = PeopleRecordSchema(many=True)


@ns.route('/cameras')
class PeopleCameras(Resource):
    def get(self):
        cams = Camera.query.filter_by(type=CameraType.PEOPLE_TRAFFIC_COUNTING).all()
        return [{'id': c.id, 'name': c.name} for c in cams]


@ns.route('/cameras/<int:camera_id>')
class PeopleByCamera(Resource):
    def get(self, camera_id):
        from_date = datetime.strptime(ns.payload.get('from_date'), '%Y-%m-%d')
        to_date = datetime.strptime(ns.payload.get('to_date'), '%Y-%m-%d')
        records = PeopleRecord.query.filter(
            PeopleRecord.camera_id == camera_id,
            PeopleRecord.created_at >= from_date,
            PeopleRecord.created_at <= to_date
        ).all()
        return schema_many.dump(records)


@ns.route('/cameras/<int:camera_id>/hourly')
class PeopleHourly(Resource):
    def get(self, camera_id):
        date = datetime.strptime(ns.payload.get('date'), '%Y-%m-%d')
        next_day = date.replace(hour=23, minute=59, second=59)
        records = PeopleRecord.query.filter(
            PeopleRecord.camera_id == camera_id,
            PeopleRecord.created_at >= date,
            PeopleRecord.created_at <= next_day
        ).all()
        return schema_many.dump(records)
# people_resource.py
