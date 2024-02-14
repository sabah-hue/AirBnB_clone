#!/usr/bin/python3
""" model test for city class """
from models.base_model import BaseModel
import unittest
from models.user import City


class TestClassCityunittest.TestCase):
    """ test case for city class by unittest """
     def test_sub_class(self):
         """ test if basemodel is parent """
         self.assertTrue(issubclass(City, BaseModel))
