#!/usr/bin/python3
"""
Base module for AirBnB project
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base model class"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """instantiation"""
        if kwargs:
            if "__class__" not in kwargs.keys():
                setattr(self, "__class__", self.__class__.__name__)
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        setattr(self, key, datetime.now())
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """should print:
        [<class name>] (<self.id>) <self.__dict__>"""
        self.__dict__["id"] = self.id
        self.__dict__["created_at"] = self.created_at
        self.__dict__["updated_at"] = self.updated_at
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at
        with current datetime"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        dict_1 = self.__dict__.copy()
        dict_1['created_at'] = self.created_at.isoformat()
        dict_1['updated_at'] = self.updated_at.isoformat()
        dict_1["__class__"] = self.__class__.__name__
        return dict_1
