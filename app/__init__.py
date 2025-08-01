from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from app.database import db
from app.resources import (
    camera_resource,
    roi_resource,
    people_resource,
    rasta_resource,
    food_resource,
    animal_resource
)

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://smartuser:smartpass123@localhost/smartcam'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app, doc='/docs')
    api.add_namespace(camera_resource.ns, path='/cameras')
    api.add_namespace(roi_resource.ns, path='/rois')
    api.add_namespace(people_resource.ns, path='/people_records')
    api.add_namespace(rasta_resource.ns, path='/rasta_records')
    api.add_namespace(food_resource.ns, path='/food_records')
    api.add_namespace(animal_resource.ns, path='/animal_records')

    return app
