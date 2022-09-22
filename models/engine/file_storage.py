#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    '''Serializes and deserializes json files'''

    __file.path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User":User, "Place": place,
            "Amenity": Amenity, "city": City, "Review": Review,
            "State":State}

    def all(self):
        return self.__objects
    def new(self, obj):
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__,obj.id)
            self.__objects[key] = obj
    def save(self):
        my_dict = {}:

            for key, obj in self.objects.items():
                my_dict[key] = obj.to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(my_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val
                self.objects[key] = obj
        except FileNotFoundError:
            pass
                


