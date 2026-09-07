#!/usr/bin/python3
"""FileStorage class module"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes and deserializes objects to/from JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects"""
        return self.__objects

    def new(self, obj):
        """Add object to storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Save all objects to JSON file"""
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """Load objects from JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, dict_obj in data.items():
                    class_name = dict_obj['__class__']
                    classes = {
                        'BaseModel': BaseModel,
                        'User': User,
                        'Place': Place,
                        'State': State,
                        'City': City,
                        'Amenity': Amenity,
                        'Review': Review
                    }
                    cls = classes.get(class_name)
                    if cls:
                        obj = cls(**dict_obj)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
