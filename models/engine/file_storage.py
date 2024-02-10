#!/usr/bin/python3
""" FileStorage module """

from models.base_model import BaseModel
import json


class FileStorage:
    """ to store data and retrive again """
    def __init__(self, file_path, objects):
        """ constractor """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ return all objects """
        return self.__objects

    def new(self, obj):
        """ add new object to dictionary """
        key_1 = obj.__class__.__name__
        key_2 = obj.id
        full_key = f"{key_1}.{key_2}"
        self.__objects[fuu_key] = obj

    def save(self):
        """ save dictionary in json file """
        dictionary = {}
        for k, v in self.__objects.items():
            dictionary[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(self.__file_path, f)

    def reload(self):
        """ retrive data from json file """
        try:
            with open(self.__file_path, "r") as f:
                dic_data = json.load(f)

        except Exception:
            pass
