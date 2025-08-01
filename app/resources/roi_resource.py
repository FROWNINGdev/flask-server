# 📄 app/resources/roi_resource.py
from flask_restx import Namespace, Resource, fields
from app.models.camera_roi import ROI
from app.schemas.roi_schema import ROISchema
from app.database import db

ns = Namespace('ROIs', description='ROI зоны')
schema = ROISchema()
schema_many = ROISchema(many=True)

roi_model = ns.model('ROI', {
    'id': fields.Integer(readonly=True),
    'name': fields.String,
    'geometry': fields.Raw,
    'type': fields.String(enum=['RASTA', 'FOOD', 'ANIMAL'])
})


@ns.route('')
class ROIList(Resource):
    def get(self, camera_id):
        join_ids = [c.roi_id for c in CameraROI.query.filter_by(camera_id=camera_id)]
        return schema_many.dump(ROI.query.filter(ROI.id.in_(join_ids)).all())

    @ns.expect(roi_model)
    def post(self, camera_id):
        roi = schema.load(ns.payload, session=db.session)
        db.session.add(roi)
        db.session.flush()
        db.session.add(CameraROI(camera_id=camera_id, roi_id=roi.id))
        db.session.commit()
        return schema.dump(roi), 201


@ns.route('/<int:roi_id>')
class ROIDetail(Resource):
    def get(self, camera_id, roi_id):
        return schema.dump(ROI.query.get_or_404(roi_id))

    def put(self, camera_id, roi_id):
        roi = ROI.query.get_or_404(roi_id)
        updated = schema.load(ns.payload, instance=roi, session=db.session)
        db.session.commit()
        return schema.dump(updated)

    def delete(self, camera_id, roi_id):
        roi = ROI.query.get_or_404(roi_id)
        CameraROI.query.filter_by(camera_id=camera_id, roi_id=roi_id).delete()
        db.session.delete(roi)
        db.session.commit()
        return '', 204
# roi_resource.py
