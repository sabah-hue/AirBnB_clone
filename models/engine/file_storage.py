#!/usr/bin/python3
""" FileStorage module """

from models.base_model import BaseModel
import json


class FileStorage:
    """ to store data and retrive again """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return all objects """
        return self.__objects

    def new(self, obj):
        """ add new object to dictionary """
        key_1 = obj.__class__.__name__
        key_2 = obj.id
        full_key = f"{key_1}.{key_2}"
        self.__objects[full_key] = obj

    def save(self):
        """ save dictionary in json file """
        dictionary = {}
        for k, v in self.__objects.items():
            dictionary[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dictionary, f)

    def reload(self):
        """ retrive data from json file """
        try:
            with open(self.__file_path, "r") as f:
                dic_data = json.load(f)
            for k, v in dic_data.items():
                v = eval(v["__class__"])(**v)
                self.__objects[k] = v
        except Exception:
            pass
