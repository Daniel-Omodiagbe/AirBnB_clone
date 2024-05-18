#!/usr/bin/python3
"""
storgae module for AirBnB project
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """ stores data using JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """add new objects to __objects"""
        if obj:
            name = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[name] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        new_dict = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file back to dict"""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    if hasattr(models, class_name):
                        self.__objects[key] = getattr(models, class_name)(**val)
        except FileNotFoundError:
            pass
