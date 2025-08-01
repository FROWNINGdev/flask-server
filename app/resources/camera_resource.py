# 📄 app/resources/camera_resource.py
from flask_restx import Namespace, Resource, fields
from app.models.camera import Camera
from app.schemas.camera_schema import CameraSchema
from app.database import db

ns = Namespace('Cameras', description='Управление камерами')
schema = CameraSchema()
schema_many = CameraSchema(many=True)

camera_model = ns.model('Camera', {
    'id': fields.Integer(readonly=True),
    'name': fields.String,
    'ip': fields.String,
    'username': fields.String,
    'password': fields.String,
    'type': fields.String(enum=['PEOPLE_TRAFFIC_COUNTING', 'RASTA', 'FOOD', 'ANIMAL_CLASSIFIER'])
})

@ns.route('')
class CameraList(Resource):
    def get(self):
        return schema_many.dump(Camera.query.all())

    @ns.expect(camera_model)
    def post(self):
        camera = schema.load(ns.payload, session=db.session)
        db.session.add(camera)
        db.session.commit()
        return schema.dump(camera), 201

@ns.route('/<int:id>')
class CameraDetail(Resource):
    def get(self, id):
        return schema.dump(Camera.query.get_or_404(id))

    def put(self, id):
        camera = Camera.query.get_or_404(id)
        updated = schema.load(ns.payload, instance=camera, session=db.session)
        db.session.commit()
        return schema.dump(updated)

    def delete(self, id):
        camera = Camera.query.get_or_404(id)
        db.session.delete(camera)
        db.session.commit()
        return '', 204