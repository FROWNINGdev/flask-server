from flask import Flask
from flask_restx import Api
from app.database import db
from app.resources.camera_resource import ns as camera_ns
from app.resources.roi_resource import ns as roi_ns
from app.resources.people_resource import ns as people_ns
from app.resources.rasta_resource import ns as rasta_ns
from app.resources.food_resource import ns as food_ns
from app.resources.animal_resource import ns as animal_ns

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/smartcam'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api = Api(app, doc='/docs')
    api.add_namespace(camera_ns, path='/cameras')
    api.add_namespace(roi_ns, path='/rois')
    api.add_namespace(people_ns, path='/people_records')
    api.add_namespace(rasta_ns, path='/rasta_records')
    api.add_namespace(food_ns, path='/food_records')
    api.add_namespace(animal_ns, path='/animal_records')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
