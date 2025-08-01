# 📄 app/resources/__init__.py
from .camera_resource import ns as camera_ns
from .roi_resource import ns as roi_ns
from .people_resource import ns as people_ns
from .rasta_resource import ns as rasta_ns
from .food_resource import ns as food_ns
from .animal_resource import ns as animal_ns

def register_resources(api):
    api.add_namespace(camera_ns, path='/cameras')
    api.add_namespace(roi_ns, path='/cameras/<int:camera_id>/rois')
    api.add_namespace(people_ns, path='/people_records')
    api.add_namespace(rasta_ns, path='/rasta_records')
    api.add_namespace(food_ns, path='/food_records')
    api.add_namespace(animal_ns, path='/animal_records')