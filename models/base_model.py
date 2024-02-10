#!/usr/bin/python3
""" base model for other classes """

import uuid
from datetime import datetime

class BaseModel:
    """ base class for other classes """
    def __init__(self, *args, **kwargs):
        """ class constactor """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, "created_at", value)
                    if key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, "updated_at", value)
                    setattr(self, key, value)
                if "id" not in kwargs.keys():
                    id_value = str(uuid.uuid4())
                    setattr(self, "id", id_value)
                if "created_at" not in kwargs.keys():
                    value = datetime.now()
                    setattr(self, "created_at", value)
                if "updated_at" not in kwargs.keys():
                    value = datetime.now()
                    setattr(self, "updated_at", value)


    def __str__(self):
        """ print string """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update the attribute updated at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ convert to dictionary """
        dict_data = self.__dict__.copy()
        dict_data['__class__'] = type(self).__name__
        dict_data['created_at'] = self.created_at.isoformat()
        dict_data['updated_at'] = self.updated_at.isoformat()
        return dict_data
