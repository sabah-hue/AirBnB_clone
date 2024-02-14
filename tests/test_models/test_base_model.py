#!/usr/bin/python3
""" unit test for base model """
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ test case for base model """
    def test_id_type(self):
        """ test id is string """
        self.assertTrue(type(BaseModel().id) is str)

    def test_created_at(self):
        """ test created at is time """
        self.assertTrue(isinstance(BaseModel().created_at, datetime))

    def test_updated_at(self):
        """ test updated at is time """
        self.assertTrue(isinstance(BaseModel().updated_at, datetime))

    def test_todict_type(self):
        """ test to dict is dictionary """
        self.assertTrue(type(BaseModel().to_dict()), dict)

    def test_assign_value(self):
        """ test assign value to property """
        BaseModel.my_number = 89
        BaseModel.name = "sabah"
        self.assertEqual(BaseModel.my_number, 89)
        self.assertEqual(BaseModel.name, "sabah")

    def test_model(self):
        """ test if instance from object is type model """
        instance_model = BaseModel()
        self.assertTrue(isinstance(instance_model, BaseModel))

    def test_uniqe_id(self):
        """ test uniqe id for each instance from class """
        first = BaseModel()
        second = BaseModel()
        self.assertNotEqual(first.id, second.id)

    def test_save_function(self):
        """ test save function """
        instance_model = BaseModel()
        first = instance_model.updated_at
        instance_model.save()
        second = instance_model.updated_at
        self.assertNotEqual(first, second)

    def test_string(self):
        """ test __str__ output """
        i_model = BaseModel()
        output = "[BaseModel] ({}) {}".format(i_model.id, i_model.__dict__)
        self.assertEqual(output, str(i_model))

    def test_to_dict_function(self):
        """ test data convert to dictionary type """
        i_model = BaseModel()
        dict_data = i_model.to_dict()
        self.assertTrue(isinstance(dict_data, dict))

    def test_
